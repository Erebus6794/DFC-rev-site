from rxconfig import config
import reflex as rx


styles = {
    "site_bg": {
        "background_image": "bg.png",
        "background_size": "cover",
        "background_position": "center",
        "position": "relative",
        "height": "100vh",
        "width": "100%",
    },
}


class State(rx.State):
    sol: int


def index():
    return rx.center(
        rx.vstack(
            rx.heading("Degen Fat Cats Revenue Distribution",
                       font_size="2em", color="#ffca40"),
            rx.link(
                "DFC Discord",
                color="#ffca40",
                href="https://discord.gg/degenfatcats",
                rel="noreferrer noopener",
                is_external=True,
                border="0.1em solid",
                padding="0.5em",
                border_radius="0.5em",
                _hover={
                    "color": "rgb(107,99,246)",
                },
            ),
            rx.text("Enter Your Fatcat Wallet Address:", color="#000000"),
            rx.hstack(
                rx.input(
                    on_change=State.set_sol,
                    color="#ffca40",
                    width="450px",
                ),
            ),
            rx.table(
                rx.tbody(
                    rx.tr(
                        rx.td("Total Sol per Fat Cat", color="#000000"),
                        rx.td("4.543", "Sol", color="#000000"),
                    )
                ),
                rx.tbody(
                    rx.tr(
                        rx.td("Total Sol Generated", color="#000000"),
                        rx.td("159563.33", "Sol", color="#000000"),
                    )
                ),
                rx.tbody(
                    rx.tr(
                        rx.td("Total Sol to Reserve", color="#000000"),
                        rx.td("5665.441", "Sol", color="#000000"),
                    )
                ),
                rx.tbody(
                    rx.tr(
                        rx.td("Total Sol to Cold Wallet", color="#000000"),
                        rx.td("12106.527", "Sol", color="#000000"),
                    )
                ),
                rx.tbody(
                    rx.tr(
                        rx.td("Total Sol to Marketing", color="#000000"),
                        rx.td("15555.71", "Sol", color="#000000"),
                    )
                ),
                rx.tbody(
                    rx.tr(
                        rx.td("Total Sol to Player Rewards Fund",
                              color="#000000"),
                        rx.td("11541.9", "Sol", color="#000000"),
                    )
                ),
                rx.tbody(
                    rx.tr(
                        rx.td("Total Sol to Contingency Fund", color="#000000"),
                        rx.td("5770.98", "Sol", color="#000000"),
                    )
                ),
                rx.tbody(
                    rx.tr(
                        rx.td("Total DCF Sol to Partner Projects",
                              color="#000000"),
                        rx.td("7510.221", "Sol", color="#000000"),
                    )
                ),
            ),
            rx.hstack(
                rx.image(
                    src="411.png",
                    width="60px",
                    height="auto",
                    border_radius="15px 15px",
                    border="3px solid #ffca40",
                    box_shadow="lg",
                ),
                rx.text(
                    "Created By Erebus. Follow me on",
                    font_size="1em",
                    color="#000000",
                    height="40px"
                ),
                rx.link(
                    rx.hstack(rx.text("Twitter", font_size="1em",
                              height="40px", color="#0071FF")),
                    href="https://twitter.com/erebus6794",
                    rel="noreferrer noopener",
                    is_external=True,
                ),
            ),
            spacing="1.5em",
            font_size="1.5em",
        ),
        style=styles["site_bg"],
    )


app = rx.App()
app.add_page(index)
