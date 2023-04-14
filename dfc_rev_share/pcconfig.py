import pynecone as pc

config = pc.Config(
    app_name="dfc_rev_share",
    db_url="sqlite:///pynecone.db",
    env=pc.Env.DEV,
)
