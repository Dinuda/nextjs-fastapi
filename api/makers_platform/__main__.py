import uvicorn

from makers_platform.settings import settings


def main() -> None:
    """Entrypoint of the application."""
    uvicorn.run(
        "makers_platform.web.application:get_app",
        workers=settings.workers_count,
        host=settings.host, # 0.0.0.0 for Docker
        port=settings.port,
        reload=settings.reload,
        log_level=settings.log_level.lower(),
        factory=True,
    )


if __name__ == "__main__":
    main()
