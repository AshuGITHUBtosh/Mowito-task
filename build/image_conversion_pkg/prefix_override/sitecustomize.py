import sys
if sys.prefix == '/usr':
    sys.real_prefix = sys.prefix
    sys.prefix = sys.exec_prefix = '/home/ashutosh/Desktop/camera_ws/install/image_conversion_pkg'
