from sqlalchemy.orm import Session

from models.user_memory import UserMemory


def save_memory(
    db: Session,
    user_id: int,
    memory_type: str,
    memory_value: str
):

    existing_memory = (
        db.query(UserMemory)
        .filter(
            UserMemory.user_id == user_id,
            UserMemory.memory_type == memory_type,
            UserMemory.memory_value == memory_value
        )
        .first()
    )

    if existing_memory:
        return existing_memory

    memory = UserMemory(
        user_id=user_id,
        memory_type=memory_type,
        memory_value=memory_value
    )

    db.add(memory)
    db.commit()
    db.refresh(memory)

    return memory


def get_user_memories(
    db: Session,
    user_id: int
):

    memories = (
        db.query(UserMemory)
        .filter(
            UserMemory.user_id == user_id
        )
        .all()
    )

    return memories


def extract_and_save_memory(
    db: Session,
    user_id: int,
    message: str
):

    message_lower = message.lower()

    # Preferred programming language
    if "python" in message_lower:

        save_memory(
            db,
            user_id,
            "preferred_language",
            "Python"
        )

    # Career interest
    if "ai/ml" in message_lower or "machine learning" in message_lower:

        save_memory(
            db,
            user_id,
            "career_interest",
            "AI/ML"
        )

    # FastAPI interest
    if "fastapi" in message_lower:

        save_memory(
            db,
            user_id,
            "technology",
            "FastAPI"
        )

    # Generative AI interest
    if "generative ai" in message_lower:

        save_memory(
            db,
            user_id,
            "technology",
            "Generative AI"
        )

    # Job role
    if "ai engineer" in message_lower:

        save_memory(
            db,
            user_id,
            "job_role",
            "AI Engineer"
        )

    if "ml engineer" in message_lower:

        save_memory(
            db,
            user_id,
            "job_role",
            "ML Engineer"
        )

    # Interview preparation
    if "interview" in message_lower:

        save_memory(
            db,
            user_id,
            "interview_preparation",
            "Interview preparation"
        )

    # Learning preference
    if "step by step" in message_lower:

        save_memory(
            db,
            user_id,
            "learning_preference",
            "Step-by-step learning"
        )