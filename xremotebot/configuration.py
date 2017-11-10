from utilconfig import days, hours, minutes, seconds, random_secret
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
log_level = 'INFO'
log_file = 'xremotebot.log'
port = 8000
public_server = False
api_key_expiration = days(700)
reservation_expiration = seconds(60)
robots = {
    'n6': [1, 6]
}

# STREAMING
disable_streaming = False
camera_device = '/dev/video0'
framerate = '30'
resolution = '352x288'
use_embed_streaming = True
# embed_streaming = '''<iframe width="1280" height="720" src="https://www.youtube.com/embed/rSJxeVlWI0c?autoplay=1" frameborder="0" gesture="media" allowfullscreen></iframe><br/><a href="https://www.youtube.com/channel/UC55u3yo0q8uJsqJJlhWQD0g/live">Ver en YouTube</a>'''
embed_streaming = '''<iframe width="1280" height="720" src="https://www.youtube.com/embed/live_stream?channel=UC55u3yo0q8uJsqJJlhWQD0g&autoplay=1" frameborder="0" gesture="media" allowfullscreen></iframe><br/><a href="https://www.youtube.com/channel/UC55u3yo0q8uJsqJJlhWQD0g/live">Ver en YouTube</a>'''
hostname = '163.10.20.156' # 'xremotebot.example'
video_ws_port = 8084
video_ws = 'ws://{}:{}/'.format(hostname, video_ws_port)
