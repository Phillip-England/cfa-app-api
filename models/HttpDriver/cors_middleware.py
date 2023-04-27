from fastapi.middleware.cors import CORSMiddleware


def cors_middleware(self):
    origins = ["*"]
    self.app.add_middleware(
        CORSMiddleware,
        allow_origins=origins,
        allow_credentials=True,
        allow_methods=["*"],
        allow_headers=["*"],
    )
    return self
