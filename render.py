import asyncio, pathlib
from playwright.async_api import async_playwright
J=[("banner_1920x1080",1920,1080,False),("banner_square_1080",1080,1080,False),("session_lineup_1560",1560,900,True)]
async def main():
    async with async_playwright() as p:
        b=await p.chromium.launch(executable_path='/opt/pw-browsers/chromium') if pathlib.Path('/opt/pw-browsers/chromium').is_file() else await p.chromium.launch()
        for n,w,h,full in J:
            pg=await b.new_page(viewport={'width':w,'height':h})
            await pg.goto(pathlib.Path(f'images/src/{n}.html').resolve().as_uri()); await pg.wait_for_timeout(300)
            await pg.screenshot(path=f'images/{n}.png',full_page=full)
        await b.close()
asyncio.run(main())
