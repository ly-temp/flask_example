from flask import Blueprint,request
bp = Blueprint('folder', __name__, url_prefix='/folder')

import os
os.chdir(os.path.join(bp.root_path, 'some-subfolder'))
cwd = os.getcwd()

@bp.route('/')
def index():
  return '/folder'
