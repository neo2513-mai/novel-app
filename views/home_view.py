import flet as ft
from config import READAWRITE_URL, MESSENGER_URL

def build_home_view(page, episodes_data, on_select_episode, on_refresh=None):
    # Header Banner
    header_banner = ft.Container(
        gradient=ft.LinearGradient(
            begin=ft.Alignment(-1.0, -1.0),
            end=ft.Alignment(1.0, 1.0),
            colors=["#E2E2FB", "#FFDEE9", "#B5FFFC"],
        ),
        padding=ft.Padding(left=12, top=10, right=12, bottom=10),
        content=ft.Column(
            controls=[
                ft.Row(
                    wrap=True,
                    alignment=ft.MainAxisAlignment.START,
                    vertical_alignment=ft.CrossAxisAlignment.CENTER,
                    spacing=8,
                    run_spacing=5,
                    controls=[
                        ft.Image(
                            src="https://i.ibb.co/3t8y0k0/logo2.png",
                            width=110,
                            height=50,
                            fit="contain",
                        ),
                        ft.Row(
                            spacing=2,
                            tight=True,
                            controls=[
                                ft.Icon(ft.Icons.PHONE, color=ft.Colors.GREEN, size=15),
                                ft.Text(
                                    "094-6702121",
                                    size=15,
                                    weight=ft.FontWeight.BOLD,
                                    color=ft.Colors.BLACK_87,
                                ),
                            ],
                        ),
                        ft.Column(
                            horizontal_alignment=ft.CrossAxisAlignment.CENTER,
                            spacing=0,
                            tight=True,
                            controls=[
                                ft.Image(
                                    src="https://i.ibb.co/LXcTngFN/jasline.jpg",
                                    width=35,
                                    height=35,
                                    fit="contain",
                                ),
                                ft.Text(
                                    "สแกน Line QR",
                                    size=15,
                                    weight=ft.FontWeight.BOLD,
                                    color=ft.Colors.GREY_800,
                                ),
                            ],
                        ),
                        ft.Row(
                            controls=[
                               
                               ft.Text(
                                   spans=[
                                       ft.TextSpan(
                                       "Messenger :--  ",
                                        style=ft.TextStyle(
                                        size=14,
                                        color=ft.Colors.RED,
                                        weight=ft.FontWeight.BOLD,
                                       ),
                                    ),
                                  ft.TextSpan(
                                     "m.me/khedkhean ",
                                      style=ft.TextStyle(
                                      size=14,
                                     color=ft.Colors.BLUE,  # เปลี่ยนเฉพาะส่วนนี้เป็นสีน้ำเงิน
                                     weight=ft.FontWeight.BOLD,
                                    ),
                                 ),
                              ],
                             )
                            ],
                            vertical_alignment=ft.CrossAxisAlignment.CENTER,
                        )
                    ],
                ),
                ft.Container(height=5),
                # ⚡ เพิ่มแถบหัวข้อพร้อมปุ่ม Refresh ด้านขวา
                # ⚡ แถบหัวข้อพร้อมปุ่มและข้อความ Refresh
                ft.Row(
                    alignment=ft.MainAxisAlignment.SPACE_BETWEEN,
                    vertical_alignment=ft.CrossAxisAlignment.CENTER,
                    controls=[
                        ft.Text(
                            "นิยายอ่านฟรี...",
                            size=22,
                            weight=ft.FontWeight.BOLD,
                            color=ft.Colors.BLUE,
                        ),
                        # จัดกลุ่มไอคอนกับข้อความให้อยู่ติดกันด้านขวา
                        ft.Row(
                            spacing=2,
                            tight=True,
                            vertical_alignment=ft.CrossAxisAlignment.CENTER,
                            controls=[
                                ft.IconButton(
                                    icon=ft.Icons.REFRESH_ROUNDED,
                                    icon_color=ft.Colors.BLUE_700,
                                    icon_size=26,
                                    tooltip="รีเฟรชดึงข้อมูลล่าสุด",
                                    on_click=lambda _: on_refresh() if on_refresh else None,
                                ),
                                ft.Text(
                                    "รีเฟรซ อ่านตอนใหม่",
                                    size=13,
                                    weight=ft.FontWeight.BOLD,
                                    color=ft.Colors.BLUE_700,
                                ),
                            ],
                        ),
                    ],
                ),

                ft.Text(
                    "จินตนาการไม่มีวันจบ.. หากมันอยู่ในหัว จงฟังเสียงมัน",
                    size=14,
                    color=ft.Colors.BLACK_87,
                    weight=ft.FontWeight.BOLD,
                ),
            ]
        ),
    )

    # Episode Cards List
    cards_list = []
    if not episodes_data:
        cards_list.append(
            ft.Container(
                content=ft.Column(
                    controls=[
                        ft.ProgressRing(color=ft.Colors.BLUE),
                        ft.Text("กำลังโหลดนิยาย...", size=14, color=ft.Colors.GREY_700)
                    ],
                    horizontal_alignment=ft.CrossAxisAlignment.CENTER,
                    spacing=10
                ),
                padding=30,
                alignment=ft.Alignment(0, 0)
            )
        )
    else:
        for ep in episodes_data:
            img_url = ep.get("image_url", "").strip()
            cards_list.append(
                ft.Container(
                    bgcolor="#F2F2F2",
                    border_radius=16,
                    padding=5,
                    on_click=lambda _, episode=ep: on_select_episode(episode),
                    content=ft.Column(
                        horizontal_alignment=ft.CrossAxisAlignment.START,
                        controls=[
                            ft.Container(
                                height=250,
                                alignment=ft.Alignment(0, 0),
                                content=(
                                    ft.Image(
                                        src=img_url if img_url else "https://via.placeholder.com/200",
                                        fit="contain",
                                        border_radius=10,
                                    )
                                    if img_url
                                    else ft.Icon(
                                        ft.Icons.BOOK_ROUNDED,
                                        size=150,
                                        color=ft.Colors.GREY_400,
                                    )
                                ),
                            ),
                            ft.Container(height=10),
                            ft.Text(
                                ep.get("title", "ไม่มีชื่อตอน"),
                                size=18,
                                weight=ft.FontWeight.BOLD,
                                color=ft.Colors.BLACK,
                            ),
                            ft.Text(
                                "คลิ๊ก...อ่าน.นิยาย",
                                style=ft.TextStyle(
                                    color=ft.Colors.RED,
                                    size=25,
                                    weight=ft.FontWeight.BOLD,
                                ),
                            ),
                        ],
                    ),
                )
            )

    cards_column = ft.Container(
        padding=ft.Padding(left=20, top=15, right=20, bottom=0),
        content=ft.Column(controls=cards_list, spacing=15),
    )

    main_scrollable = ft.ListView(
        expand=True,
        controls=[
            header_banner,
            cards_column,
            ft.Container(height=20),
        ],
    )

    async def nav_change(e):
        selected_index = e.control.selected_index
        
        if selected_index == 0:
            await page.url_launcher.launch_url(READAWRITE_URL)
            e.control.selected_index = 0
            page.update()
        elif selected_index == 1:
            page.update()

    bottom_nav = ft.NavigationBar(
        bgcolor=ft.Colors.WHITE,
        elevation=0,
        selected_index=0,
        on_change=nav_change,
        destinations=[
            ft.NavigationBarDestination(
                icon=ft.Icons.SEARCH,
                label="ดูนิยายทั้งหมด",
            ),
            ft.NavigationBarDestination(
                icon=ft.Image(
                    src="https://i.ibb.co/hFcfCrhV/b1.png",
                    width=50,
                    height=50,
                ),
                label="สนับสนุนค่ากาแฟ",
            ),
        ],
    )

    return ft.View(
        route="/",
        padding=0,
        controls=[main_scrollable],
        navigation_bar=bottom_nav,
    )