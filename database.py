import aiosqlite

DB_NAME = "debida_gig.db"


async def init_db():
    async with aiosqlite.connect(DB_NAME) as db:
        await db.execute("""
        CREATE TABLE IF NOT EXISTS campaigns (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            user_id INTEGER,
            task_type TEXT,
            task_link TEXT,
            workers INTEGER,
            reward INTEGER,
            status TEXT
        )
        """)
        await db.commit()
