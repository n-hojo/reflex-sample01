import reflex as rx


def index() -> rx.Component:
    """トップページを定義します。"""
    return rx.center(
        rx.vstack(
            rx.heading("Reflex へようこそ！", size="9", color="teal.600"),
            rx.text("これは複数ページサイトのサンプルです。",
                    font_size="1.5em", color="gray.700"),
            rx.divider(),
            rx.hstack(
                rx.link(
                    # size="lg" を size="3" に変更
                    rx.button("アバウトページへ", color_scheme="blue",
                              size="3", radius="full"),
                    href="/about",
                    _hover={"text_decoration": "none"}
                ),
                rx.link(
                    # size="lg" を size="3" に変更
                    rx.button("お問い合わせページへ", color_scheme="green",
                              size="3", radius="full"),
                    href="/contact",
                    _hover={"text_decoration": "none"}
                ),
                rx.link(
                    # size="lg" を size="3" に変更
                    rx.button("タブページへ", color_scheme="purple",
                              size="3", radius="full"),
                    href="/tabs",
                    _hover={"text_decoration": "none"}
                ),
                spacing="5",
            ),
            spacing="7",
            align="center",
            padding="5",
            background_color="white",
            border_radius="xl",
            box_shadow="lg",
            max_width="600px",
            width="90%"
        ),
        height="100vh",
        width="100vw",
        background_color="gray.100",
    )


def about() -> rx.Component:
    """アバウトページを定義します。"""
    return rx.center(
        rx.vstack(
            rx.heading("私たちについて", size="9", color="purple.600"),
            rx.text("私たちはReflexを使って素晴らしいWebアプリを作成しています。",
                    font_size="1.5em", color="gray.700"),
            rx.divider(),
            rx.link(
                # size="lg" を size="3" に変更
                rx.button("ホームへ戻る", color_scheme="blue",
                          size="3", radius="full"),
                href="/",
                _hover={"text_decoration": "none"}
            ),
            spacing="7",
            align="center",
            padding="5",
            background_color="white",
            border_radius="xl",
            box_shadow="lg",
            max_width="600px",
            width="90%"
        ),
        height="100vh",
        width="100vw",
        background_color="gray.100",
    )


def contact() -> rx.Component:
    """コンタクトページを定義します。"""
    return rx.center(
        rx.vstack(
            rx.heading("お問い合わせ", size="9", color="orange.600"),
            rx.text("ご質問があれば、お気軽にお問い合わせください。",
                    font_size="1.5em", color="gray.700"),
            rx.divider(),
            rx.link(
                # size="lg" を size="3" に変更
                rx.button("ホームへ戻る", color_scheme="blue",
                          size="3", radius="full"),
                href="/",
                _hover={"text_decoration": "none"}
            ),
            spacing="7",
            align="center",
            padding="5",
            background_color="white",
            border_radius="xl",
            box_shadow="lg",
            max_width="600px",
            width="90%"
        ),
        height="100vh",
        width="100vw",
        background_color="gray.100",
    )


def tabs_page() -> rx.Component:
    """タブページのサンプル。"""
    return rx.center(
        rx.vstack(
            rx.heading("タブのサンプル", size="9", color="indigo.600"),
            rx.tabs.root(
                rx.tabs.list(
                    rx.tabs.trigger("タブ1", value="tab1"),
                    rx.tabs.trigger("タブ2", value="tab2"),
                    rx.tabs.trigger("タブ3", value="tab3"),
                ),
                rx.tabs.content(
                    rx.box(rx.text("これはタブ1のコンテンツです。"), padding="1.5em"),
                    value="tab1",
                ),
                rx.tabs.content(
                    rx.box(rx.text("これはタブ2のコンテンツです。"), padding="1.5em"),
                    value="tab2",
                ),
                rx.tabs.content(
                    rx.box(rx.text("これはタブ3のコンテンツです。"), padding="1.5em"),
                    value="tab3",
                ),
                default_value="tab1",
                width="100%",
                border="1px solid #ddd",
                border_radius="lg",
                box_shadow="sm",
            ),
            rx.divider(),
            rx.link(
                rx.button("ホームへ戻る", color_scheme="blue", size="3", radius="full"),
                href="/",
                _hover={"text_decoration": "none"}
            ),
            spacing="7",
            align="center",
            padding="5",
            background_color="white",
            border_radius="xl",
            box_shadow="lg",
            max_width="600px",
            width="90%"
        ),
        height="100vh",
        width="100vw",
        background_color="gray.100",
    )


# アプリケーションの初期化とルーティングの設定は変更なし
app = rx.App()
app.add_page(index, route="/")
app.add_page(about, route="/about")
app.add_page(contact, route="/contact")
app.add_page(tabs_page, route="/tabs")
