from pinaxai.docker.app.postgres.postgres import PostgresDb


class PgVectorDb(PostgresDb):
    # -*- App Name
    name: str = "pgvector"

    # -*- Image Configuration
    image_name: str = "pinaxlabs/pgvector"
    image_tag: str = "16"
