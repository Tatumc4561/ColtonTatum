from portfolio_proj.settings.common import *


DEBUG = False

SECRET_KEY = os.environ["SECRET_KEY"]

ALLOWED_HOSTS = ["tatum-c.herokuapp.com"]


DATABASES = {
    "default": {
        "ENGINE": os.environ["DATABASE_URL"],
    }
}
db_from_env = dj_database_url.config(conn_max_age=600)
DATABASES["default"].update(db_from_env)


# STATICFILES_STORAGE = "whitenoise.storage.CompressedManifestStaticFilesStorage"


# dropbox
# DEFAULT_FILE_STORAGE = "storages.backends.dropbox.DropBoxStorage"


# DBX_TOKEN = os.environ["DBX_TOKEN"]
# DROPBOX_OAUTH2_TOKEN = DBX_TOKEN

# DROPBOX_ROOT_PATH = "/media/"
