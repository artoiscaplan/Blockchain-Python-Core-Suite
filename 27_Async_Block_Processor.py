import asyncio

class AsyncBlockProcessor:
    async def process_block(self, block):
        await asyncio.sleep(0.1)
        return f"处理完成:{block['height']}"

async def main():
    p = AsyncBlockProcessor()
    res = await p.process_block({"height":10})
    print(res)

if __name__ == "__main__":
    asyncio.run(main())
