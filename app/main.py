from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
import uvicorn

from app.core.settings import AppSettings
from app.api.routes.api import router as api_router


def get_application() -> FastAPI:
    settings = AppSettings()

    #settings.configure_logging()

    application = FastAPI(**settings.fast_api_kwargs)

    application.add_middleware(
        CORSMiddleware,
        allow_origins=settings.allowed_hosts,
        allow_credentials=True,
        allow_methods=["*"],
        allow_headers=["*"],
    )

    application.include_router(api_router, prefix=settings.api_prefix)

    return application

app = get_application()

# For debug purposes
# if __name__=="__main__":
#     app = get_application()
#     uvicorn.run(app, host="0.0.0.0", port=8081)