from utilconfig import days, hours, random_secret
import os.path

settings = {
    # Change the cookie secret to a custom fixed value for your application
    'cookie_secret': random_secret(),
    'xsrf_cookies': True,
    'debug': True,
    'static_path': os.path.join(os.path.dirname(__file__), 'static'),
    'template_path': os.path.join(os.path.dirname(__file__), 'templates'),
    'login_url': '/login',
}
dburi = 'sqlite:///test.db'
tls = False
disable_streaming = False
camera_device = '/dev/video0'
use_embed_streaming = False
embed_streaming = '''<iframe width="360" height="302"
src="http://www.ustream.tv/embed/20521415?v=3&amp;wmode=direct&autoplay=true&quality=low&showtitle=false"
scrolling="no" frameborder="0" style="border: 0px none transparent;">
</iframe>
<br /><a href="http://www.ustream.tv"
style="font-size: 12px; line-height: 20px; font-weight: normal; text-align: left;"
target="_blank">Broadcast live streaming video on Ustream</a>'''
#embed_streaming = '''<iframe width="420" height="315" src="http://www.youtube.com/embed/lShoVjW3rz0"
# frameborder="0" allowfullscreen></iframe>'''
hostname = '190.16.204.135' # 'xremotebot.example'
video_ws_port = 8084
video_ws = 'ws://{}:{}/'.format(hostname, video_ws_port)
log_level = 'DEBUG'
log_file = 'xremotebot.log'
port = 8000
public_server = True
api_key_expiration = days(700)
reservation_expiration = hours(1)
robots = {
    'n6': [3],
    'scribbler': ['00:1E:19:01:0B:81'],
}
