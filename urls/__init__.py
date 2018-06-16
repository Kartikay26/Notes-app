from notes_app import *

from .browse import *
from .editor import *
from .api import *
from .errors import *
from .data import *
from .login import *
from .homepage import *
from .dashboard import *
from .contents import *

@app.route('/lulz')
def lulz():
	return "For da lulz!"