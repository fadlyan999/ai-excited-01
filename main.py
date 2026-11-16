import shutil, os
# copy the exciting image to output
src = os.path.join(os.path.dirname(__file__), 'entry.png')
dst = os.path.join(os.environ.get('MAKEFUN_OUTPUT_DIR', '/output'), 'entry.png')
shutil.copyfile(src, dst)
