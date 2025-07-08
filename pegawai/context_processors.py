# pegawai/context_processors.py

def background_image(request):
    return {
        'background_image_url': '/static/images/background.jpg'  # Ganti sesuai kebutuhan
    }
