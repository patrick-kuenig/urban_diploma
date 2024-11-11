from tortoise import BaseDBAsyncClient


async def upgrade(db: BaseDBAsyncClient) -> str:
    return """
        ALTER TABLE "customer" ADD "referred_by_id" INT NOT NULL;
        ALTER TABLE "customer" ADD CONSTRAINT "fk_customer_user_3a040219" FOREIGN KEY ("referred_by_id") REFERENCES "user" ("id") ON DELETE CASCADE;"""


async def downgrade(db: BaseDBAsyncClient) -> str:
    return """
        ALTER TABLE "customer" DROP FOREIGN KEY "fk_customer_user_3a040219";
        ALTER TABLE "customer" DROP COLUMN "referred_by_id";"""
