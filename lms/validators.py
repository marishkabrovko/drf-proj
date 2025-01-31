import urllib.parse

from django.core.exceptions import ValidationError


def validate_video_link(value):
    """Разрешает только ссылки на YouTube."""
    allowed_domains = ["www.youtube.com"]
    parsed_url = urllib.parse.urlparse(value)

    if parsed_url.netloc not in allowed_domains:
        raise ValidationError(f"Сторонние ресурсы запрещены: {parsed_url.netloc}")

    return value
