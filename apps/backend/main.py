from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from routers import image_processing
import uvicorn

app = FastAPI()

# Enable CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Include routers
app.include_router(image_processing.router)

if __name__ == "__main__":
    import os
    import weave

    weave.init(project_name="text_emotion_analysis")
    
    port = int(os.getenv("PORT", 7860))
    uvicorn.run("main:app", host="0.0.0.0", port=port)
