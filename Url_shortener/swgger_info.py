from drf_yasg import openapi

title = "url shortener"
description = "write orginal long url and get short url"
version = "1.0.0"

info = openapi.Info(
    title=title,
    default_version=version,
    description=description,
)
