import pynecone as pc

config = pc.Config(
    app_name="dfc_rev_share",
    api_url="http://dfcrevenue.com:8000",
    bun_path="$HOME/.bun/bin/bun",
    db_url="sqlite:///pynecone.db",
    env=pc.Env.DEV,
)
