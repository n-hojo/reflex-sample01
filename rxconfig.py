import reflex as rx

config = rx.Config(
    app_name="my_new_reflex_project",
    # frontend_port=3000,
    # backend_port=8000,
    # etc...
    # Tailwind CSSを有効にするためのプラグインを追加します。
    plugins=[
        rx.plugins.TailwindV3Plugin(),
    ],
)
