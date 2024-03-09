from fastapi import FastAPI
from user import router as user_router
from event import router as event_router
from organizator import router as organizator_router

app = FastAPI()

app.include_router(organizator_router.router, prefix="/api")  # Doğru öznitelik: router
app.include_router(event_router.router, prefix="/api")        # Doğru öznitelik: router
app.include_router(user_router.router, prefix="/api")         # Doğru öznitelik: router
