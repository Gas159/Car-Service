from redis.asyncio import Redis

redis = Redis.from_url("redis://localhost:6379")
