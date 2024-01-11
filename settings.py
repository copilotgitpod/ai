INSTALLED_APPS = [
    'corsheaders'
]

MIDDLEWARE = [
    'corsheaders.middleware.CorsMiddleware'
]

CORS_ALLOW_ALL_ORIGINS = True  # This will enable CORS for all routes
