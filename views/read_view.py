import flet as ft

def build_read_view(page, episode, on_go_home, on_back):
    content_controls = []

    if episode:
        detail_img_url = episode.get("image_url", "").strip()
        if detail_img_url:
            content_controls.append(
                ft.Image(
                    src=detail_img_url,
                    fit="contain",
                    height=300,
                    border_radius=12,
                    gapless_playback=True,
                )
            )
            content_controls.append(ft.Container(height=10))

        content_controls.append(
            ft.Text(
                value=episode.get("content", "ไม่มีเนื้อหา"),
                size=17,
                color=ft.Colors.BLACK_87,
                selectable=True,
            )
        )

        content_controls.append(ft.Container(height=20))
        content_controls.append(
            ft.Button(
                content=ft.Row(
                    controls=[
                        ft.Icon(ft.Icons.HOME_ROUNDED, color=ft.Colors.WHITE),
                        ft.Text(
                            "กลับสู่หน้าแรก",
                            size=16,
                            color=ft.Colors.WHITE,
                            weight=ft.FontWeight.BOLD,
                        ),
                    ],
                    alignment=ft.MainAxisAlignment.CENTER,
                    tight=True,
                ),
                bgcolor=ft.Colors.BLACK,
                style=ft.ButtonStyle(
                    shape=ft.RoundedRectangleBorder(radius=10),
                    padding=ft.Padding(left=20, top=12, right=20, bottom=12),
                ),
                width=250,
                on_click=lambda _: on_go_home(),
            )
        )

    page_title = episode.get("title", "อ่านนิยาย") if episode else "อ่านนิยาย"

    return ft.View(
        route="/read",
        scroll="auto",
        controls=[
            ft.AppBar(
                title=ft.Text(page_title, color=ft.Colors.BLACK),
                bgcolor=ft.Colors.WHITE,
                elevation=0,
                leading=ft.IconButton(
                    icon=ft.Icons.ARROW_BACK,
                    icon_color=ft.Colors.BLACK,
                    on_click=lambda _: on_back(),
                ),
            ),
            ft.Container(
                content=ft.Column(controls=content_controls, spacing=15),
                padding=20,
            ),
        ],
    )