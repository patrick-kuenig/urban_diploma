from tortoise import BaseDBAsyncClient


async def upgrade(db: BaseDBAsyncClient) -> str:
    return """
        CREATE TABLE IF NOT EXISTS "category" (
    "id" INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,
    "name" VARCHAR(30) NOT NULL
);
CREATE TABLE IF NOT EXISTS "customer" (
    "id" INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,
    "first_name" VARCHAR(30) NOT NULL,
    "last_name" VARCHAR(30) NOT NULL,
    "company_name" VARCHAR(30) NOT NULL,
    "email_address" VARCHAR(30) NOT NULL,
    "phone_number" VARCHAR(30) NOT NULL,
    "address" VARCHAR(50) NOT NULL,
    "comments" TEXT NOT NULL
);
CREATE TABLE IF NOT EXISTS "user" (
    "id" INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,
    "username" VARCHAR(30) NOT NULL UNIQUE,
    "password" VARCHAR(50) NOT NULL,
    "first_name" VARCHAR(30) NOT NULL,
    "last_name" VARCHAR(30) NOT NULL,
    "is_active" INT NOT NULL  DEFAULT 1
);
CREATE TABLE IF NOT EXISTS "task" (
    "id" INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,
    "name" VARCHAR(50) NOT NULL,
    "description" TEXT NOT NULL,
    "creation_date" TIMESTAMP NOT NULL  DEFAULT CURRENT_TIMESTAMP,
    "category_id" INT NOT NULL REFERENCES "category" ("id") ON DELETE CASCADE,
    "customer_id" INT NOT NULL REFERENCES "customer" ("id") ON DELETE CASCADE,
    "user_id" INT NOT NULL REFERENCES "user" ("id") ON DELETE CASCADE
);
CREATE TABLE IF NOT EXISTS "aerich" (
    "id" INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,
    "version" VARCHAR(255) NOT NULL,
    "app" VARCHAR(100) NOT NULL,
    "content" JSON NOT NULL
);"""


async def downgrade(db: BaseDBAsyncClient) -> str:
    return """
        """
