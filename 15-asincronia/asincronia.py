import asyncio
import datetime

async def asyncHello(name: str, seconds: int):
    print(f"""La funcion {name}, dura {seconds} segundos
        Indica en {datetime.datetime.now().strftime('%H:%M:%S')}""")
    await asyncio.sleep(seconds)
    print(f"La funcion {name} ha finalizado en: {datetime.datetime.now().strftime('%H:%M:%S')}")

asyncio.run(asyncHello('Test', 5))

# extra
async def ejercicioExtra():
    await asyncio.gather(
        asyncHello("C", 3),
        asyncHello("B", 2),
        asyncHello("A", 1),
    )

asyncio.run(ejercicioExtra())