from django.shortcuts import render

# Create your views here.
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status, permissions
from django.conf import settings
from .models import Website
from main.manager import IsAdminOrEditor
import openai
from .serializers import WebsiteSerializer
from bson import ObjectId
from main.manager import WebsitePermission



class GenerateWebsiteAPIView(APIView):
    permission_classes = [permissions.IsAuthenticated, IsAdminOrEditor]

    def post(self, request):
        business_type = request.data.get("business_type")
        industry = request.data.get("industry")

        if not business_type or not industry:
            return Response({"error": "Missing business_type or industry"}, status=400)

        openai.api_key = settings.OPENAI_API_KEY

        try:
            response = openai.ChatCompletion.create(
                model="gpt-3.5-turbo",
                messages=[
                    {"role": "system", "content": "You are a helpful assistant that creates website content."},
                    {"role": "user", "content": f"Generate content for a {business_type} business in the {industry} industry. Include a hero section, an about section, and a list of services."}
                ],
                temperature=0.7,
                max_tokens=500
            )

            ai_text = response.choices[0].message['content'].strip()

            # Optional: crude text-to-JSON parsing
            structured_data = {
                    "hero": f"Welcome to our {business_type.title()} in {industry.title()}!",
                    "about": ai_text.split("\n")[0],
                    "services": [line.strip("- ").strip() for line in ai_text.split("\n")[1:] if line.startswith("-")],
                    "image_url": "https://via.placeholder.com/800x300?text=Business+Banner"
                }

            website = Website(
                user_id=str(request.user.id),
                title=f"{business_type} - {industry}",
                content=structured_data
            )
            website.save()

            return Response(WebsiteSerializer(website).data, status=201)

        except Exception as e:
            return Response({"error": str(e)}, status=500)

class WebsiteListCreateAPIView(APIView):
    permission_classes = [permissions.IsAuthenticated, WebsitePermission]

    def get(self, request):
        user = request.user
        if user.role == 'admin':
            websites = Website.objects.all()
        elif user.role == 'editor':
            websites = Website.objects.filter(user_id=str(user.id))
        else:
            websites = Website.objects.all()

        serializer = WebsiteSerializer(websites, many=True)
        return Response(serializer.data)

    def post(self, request):
        if request.user.role not in ['admin', 'editor']:
            return Response({"error": "You do not have permission"}, status=403)

        data = {
            "user_id": str(request.user.id),
            "title": request.data.get("title"),
            "content": request.data.get("content", {})
        }
        website = Website(**data).save()
        serializer = WebsiteSerializer(website)
        return Response(serializer.data, status=201)


class WebsiteDetailAPIView(APIView):
    permission_classes = [permissions.IsAuthenticated, WebsitePermission]

    def get_object(self, pk):
        try:
            return Website.objects.get(id=pk)
        except Website.DoesNotExist:
            return None

    def get(self, request, pk):
        website = self.get_object(pk)
        if not website:
            return Response({"error": "Not found"}, status=404)
        return Response(WebsiteSerializer(website).data)

    def put(self, request, pk):
        website = self.get_object(pk)
        if not website:
            return Response({"error": "Not found"}, status=404)

        if request.user.role == 'viewer' or website.user_id != str(request.user.id) and request.user.role != 'admin':
            return Response({"error": "Permission denied"}, status=403)

        website.title = request.data.get("title", website.title)
        website.content = request.data.get("content", website.content)
        website.save()
        return Response(WebsiteSerializer(website).data)

    def delete(self, request, pk):
        website = self.get_object(pk)
        if not website:
            return Response({"error": "Not found"}, status=404)

        if request.user.role != 'admin':
            return Response({"error": "Only admin can delete"}, status=403)

        website.delete()
        return Response({"message": "Deleted successfully"})
    


def preview_website(request, id):
    try:
        website = Website.objects.get(id=id)
    except Website.DoesNotExist:
        return render(request, 'website/not_found.html', status=404)

    return render(request, 'website/preview.html', {
        'title': website.title,
        'hero': website.content.get('hero', ''),
        'about': website.content.get('about', ''),
        'services': website.content.get('services', []),
        'image_url': website.content.get('image_url', '') 

    })   