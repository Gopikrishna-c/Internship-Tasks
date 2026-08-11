from services.chat_memory import (
    save_message,
    get_conversation
)

from services.user_memory_service import (
    get_user_memories
)

from services.interview_progress_service import (
    get_interview_progress
)

from services.chat_service import (
    generate_response
)

from services.jd_retriever_service import (
    retrieve_jd_chunks
)

from services.rag.rag_service import (
    retrieve_documents
)


# ==================================================
# Check JD Vector Search Requirement
# ==================================================

def needs_jd_vector_search(
    user_message: str
) -> bool:

    message = user_message.lower()

    keywords = [

        "job description",
        "job description says",
        "jd",
        "required skills",
        "requirements",
        "responsibilities",
        "qualification",
        "qualifications",
        "experience required",
        "skills required",
        "role requires",
        "company requires",
        "this job",
        "this role",
        "selected job"

    ]

    return any(
        keyword in message
        for keyword in keywords
    )


# ==================================================
# Check General RAG Search Requirement
# ==================================================

def needs_rag_search(
    user_message: str
) -> bool:

    message = user_message.lower()

    keywords = [

        # Resume
        "resume",
        "my resume",

        # Skills
        "my skills",
        "my technical skills",
        "technical skills",

        # Experience
        "my experience",
        "my work experience",

        # Projects
        "my projects",
        "projects in my resume",

        # Education
        "my education",
        "my qualification",
        "my qualifications",

        # Resume/document based questions
        "according to my resume",
        "according to the document",
        "according to my document",
        "in my document"

    ]

    return any(
        keyword in message
        for keyword in keywords
    )


# ==================================================
# AI Orchestrator
# ==================================================

async def orchestrate(
    db,
    user_id: int,
    user_message: str,
    job_id: int
):

    # ==================================================
    # 1. Retrieve Conversation History
    # ==================================================

    history = get_conversation(
        user_id
    )


    # ==================================================
    # 2. Retrieve Long-Term Memory
    # ==================================================

    memories = get_user_memories(
        db,
        user_id
    )


    # ==================================================
    # 3. Retrieve Interview Progress
    # ==================================================

    progress = get_interview_progress(
        db,
        user_id
    )


    # ==================================================
    # 4. Selected Job JD Vector Search
    # ==================================================

    jd_context = ""

    jd_search_used = False


    if needs_jd_vector_search(
        user_message
    ):

        try:

            relevant_chunks = retrieve_jd_chunks(

                question=user_message,

                job_id=job_id,

                top_k=2

            )

            if relevant_chunks:

                jd_context = "\n\n".join(
                    relevant_chunks
                )

                jd_search_used = True


        except Exception as e:

            print(
                f"JD Vector DB search error: {e}"
            )

            jd_context = ""


    # ==================================================
    # 5. General RAG Search
    # ==================================================

    rag_context = ""

    rag_search_used = False


    if needs_rag_search(
        user_message
    ):

        try:

            relevant_documents = retrieve_documents(

                user_message,

                top_k=3

            )

            if relevant_documents:

                rag_context = "\n\n".join(
                    relevant_documents
                )

                rag_search_used = True


        except Exception as e:

            print(
                f"RAG search error: {e}"
            )

            rag_context = ""


    # ==================================================
    # 6. Combine Retrieved Context
    # ==================================================

    vector_context = ""


    if jd_context:

        vector_context += (

            "SELECTED JOB DESCRIPTION CONTEXT:\n"

            + jd_context

        )


    if rag_context:

        if vector_context:

            vector_context += "\n\n"


        vector_context += (

            "RESUME / DOCUMENT CONTEXT:\n"

            + rag_context

        )


    # ==================================================
    # 7. Save User Message
    # ==================================================

    save_message(

        user_id,

        "user",

        user_message

    )


    # ==================================================
    # 8. Generate AI Response
    # ==================================================

    response = await generate_response(

        user_message=user_message,

        conversation_history=history,

        long_term_memories=memories,

        interview_progress=progress,

        vector_context=vector_context

    )


    # ==================================================
    # 9. Save AI Response
    # ==================================================

    save_message(

        user_id,

        "assistant",

        response

    )


    # ==================================================
    # 10. Get Updated Conversation
    # ==================================================

    updated_history = get_conversation(

        user_id

    )


    # ==================================================
    # 11. Return Complete Result
    # ==================================================

    return {

        "user_id": user_id,

        "job_id": job_id,

        "user_message": user_message,

        "response": response,

        "jd_search_used": jd_search_used,

        "rag_search_used": rag_search_used,

        "long_term_memory": [

            {

                "type": memory.memory_type,

                "value": memory.memory_value

            }

            for memory in memories

        ],

        "interview_progress": [

            {

                "topic": item.topic,

                "status": item.status

            }

            for item in progress

        ],

        "conversation_history": updated_history

    }