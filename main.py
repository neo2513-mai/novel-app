import flet as ft
import json
import os
from api import fetch_episodes
from views.home_view import build_home_view
from views.read_view import build_read_view

CACHE_FILE = "episodes_cache.json"

def main(page: ft.Page):
    page.title = "Peemai นิยายอ่านฟรี"
    page.theme_mode = ft.ThemeMode.LIGHT
    page.padding = 0
    page.spacing = 0

    state = {
        "episodes_data": [],
        "current_episode": None,
    }

    # 1. อ่าน Cache จากไฟล์ JSON
    if os.path.exists(CACHE_FILE):
        try:
            with open(CACHE_FILE, "r", encoding="utf-8") as f:
                cached = json.load(f)
                if isinstance(cached, list):
                    state["episodes_data"] = cached
        except Exception as err:
            print(f"Cache load warning: {err}")

    def open_episode(ep):
        state["current_episode"] = ep
        page.route = "/read"
        route_change()

    def go_home():
        state["current_episode"] = None
        page.route = "/"
        route_change()

    def view_pop(e=None):
        if len(page.views) > 1:
            page.views.pop()
            page.route = page.views[-1].route
            route_change()
        else:
            go_home()

    def route_change(e=None):
        page.views.clear()

        if page.route == "/":
            page.views.append(
                build_home_view(
                    page,
                    episodes_data=state["episodes_data"],
                    on_select_episode=open_episode,
                )
            )
        elif page.route == "/read":
            page.views.append(
                build_read_view(
                    page,
                    episode=state["current_episode"],
                    on_go_home=go_home,
                    on_back=view_pop,
                )
            )

        page.update()

    # 2. ปรับกลับเป็น def ธรรมดาเพื่อให้ api.py เรียกใช้ได้โดยตรง
    def on_bg_fetch_complete(new_data):
        if new_data and new_data != state["episodes_data"]:
            state["episodes_data"] = new_data
            
            # บันทึกลงไฟล์ JSON
            try:
                with open(CACHE_FILE, "w", encoding="utf-8") as f:
                    json.dump(new_data, f, ensure_ascii=False)
            except Exception as err:
                print(f"Save cache error: {err}")

            if page.route == "/":
                route_change()

    page.on_route_change = route_change
    page.on_view_pop = view_pop

    page.route = "/"
    route_change()

    # ดึงข้อมูลเบื้องหลัง
    page.run_thread(fetch_episodes, page, on_bg_fetch_complete)


if __name__ == "__main__":
    ft.run(main)