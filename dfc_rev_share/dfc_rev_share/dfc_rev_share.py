from pcconfig import config
import pynecone as pc


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


class State(pc.State):

    pass


def index():
    return pc.center(
        pc.vstack(
            pc.heading("Degen Fat Cats Revenue Distribution",
                       font_size="2em", color="#ffca40"),
            pc.link(
                "DFC Discord",
                color="#ffca40",
                href="https://discord.gg/degenfatcats",
                border="0.1em solid",
                padding="0.5em",
                border_radius="0.5em",
                _hover={
                    "color": "rgb(107,99,246)",
                },
            ),
            pc.table(
                pc.tbody(
                    pc.tr(
                        pc.td("Total Sol per Fat Cat", color="#000000"),
                        pc.td(3.9818, "Sol", color="#000000"),
                    )
                ),
                pc.tbody(
                    pc.tr(
                        pc.td("Total Sol Generated", color="#000000"),
                        pc.td(138570.97, "Sol", color="#000000"),
                    )
                ),
                pc.tbody(
                    pc.tr(
                        pc.td("Total Sol to Reserve", color="#000000"),
                        pc.td(4915.716, "Sol", color="#000000"),
                    )
                ),
                pc.tbody(
                    pc.tr(
                        pc.td("Total Sol to Cold Wallet", color="#000000"),
                        pc.td(11502.912, "Sol", color="#000000"),
                    )
                ),
                pc.tbody(
                    pc.tr(
                        pc.td("Total Sol to Marketing", color="#000000"),
                        pc.td(13487.78, "Sol", color="#000000"),
                    )
                ),
                pc.tbody(
                    pc.tr(
                        pc.td("Total Sol to Player Rewards Fund",
                              color="#000000"),
                        pc.td(9473.97, "Sol", color="#000000"),
                    )
                ),
                pc.tbody(
                    pc.tr(
                        pc.td("Total Sol to Contingency Fund", color="#000000"),
                        pc.td(4737.01, "Sol", color="#000000"),
                    )
                ),
                pc.tbody(
                    pc.tr(
                        pc.td("Total DCF Sol to Partner Projects",
                              color="#000000"),
                        pc.td(5837.539, "Sol", color="#000000"),
                    )
                ),
            ),
            pc.image(
                src="411.png",
                width="100px",
                height="auto",
                border_radius="25px 25px",
                border="3px solid #ffca40",
                box_shadow="lg",
            ),
            pc.hstack(
                pc.text(
                    "Created By Erebus.",
                    font_size="1em",
                    color="#000000",
                    height="15px"
                ),
                pc.link(
                    pc.hstack(pc.text("My Twitter", font_size="1em",
                              height="15px", color="#000000")),
                    href="https://twitter.com/erebus20080111",
                ),
            ),
            spacing="1.5em",
            font_size="1.5em",
        ),
        style=styles["site_bg"],
    )


app = pc.App(state=State)
app.add_page(index, title="DFC Revenue",
             description="Rev share display by @Erebus")
app.compile()
