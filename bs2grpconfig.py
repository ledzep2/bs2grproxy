# BS2 GAE Reverse Proxy
# Russell <yufeiwu@gmail.com>
# Please use wisely


from google.appengine.ext import db

# You can set them later directly in Database
# HTML target url
TARGET_HOST = "code.google.com"
# Cache check option. value can be 'EOD' or 0 <= number.
# EOD: start checking after the end of the day (So 1 time per day)
# 0: Check every time
# x: Check every x day (After 24 * x hours)
CACHE_CHECK = 'EOD'
# Cache static files, Only work when REDIRECTs are disabled
CACHE_STATIC = True
# Common RE
CACHABLE_RE = '.*\.(jpg|jpeg|gif|png|ico|tif|bmp|css|js)$'
IMAGES_RE = '.*\.(jpg|jpeg|gif|png|ico|tif|bmp)$'
CSSJS_RE = '.*\.(css|js)$'
MMEDIA_RE = '.*\.(avi|mov|mp3|rm|rmvb|qt|mkv)$'

"""
"""
class BS2GRPConfig(db.Model):
    target_host = db.StringProperty(required=True)
    cache_static = db.BooleanProperty(required=False, default=False)
    cachable_re = db.StringProperty(required=False, default='')
    cache_check = db.StringProperty(required=False)
    filter1_re = db.StringProperty(required=False, default='')
    filter1_redirect = db.StringProperty(required=False, default='')
    filter2_re = db.StringProperty(required=False, default='')
    filter2_redirect = db.StringProperty(required=False, default='')
    filter3_re = db.StringProperty(required=False, default='')
    filter3_redirect = db.StringProperty(required=False, default='')
    referrer_re = db.StringProperty(required=False, default='')
    referrer_redirect = db.StringProperty(required=False, default='')
    retry = db.IntegerProperty(required=False, default=2)

    REFERRER_REDIRECT = 'www.google.com'

    @staticmethod
    def get_config():
        ret = BS2GRPConfig.all().get()
        if not ret:
            config = BS2GRPConfig(
                target_host=TARGET_HOST,
                cache_static=CACHE_STATIC,
                cachable_re=CACHABLE_RE,
                cache_check=CACHE_CHECK,
                filter1_re=IMAGES_RE,
                filter2_re=CSSJS_RE,
                filter3_re=MMEDIA_RE,
            )
            config.put()
        else:
            config = ret
        return config
