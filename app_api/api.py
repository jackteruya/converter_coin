from ninja import NinjaAPI

from app_api.app.api import router as converter_router

api = NinjaAPI()


api.add_router("", converter_router)
