from backend.database import engine
from backend.models import Base


def init_db():
    Base.metadata.create_all(engine)
    print("Graph in database initialized successfully.")


if __name__ == "__main__":
    init_db()