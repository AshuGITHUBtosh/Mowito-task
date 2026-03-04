from setuptools import setup
from glob import glob
import os

package_name = 'image_conversion_pkg'

setup(
    name=package_name,
    version='0.0.0',
    packages=[package_name],
    data_files=[
        ('share/ament_index/resource_index/packages',
            ['resource/' + package_name]),
        ('share/' + package_name, ['package.xml']),

        (os.path.join('share', package_name, 'launch'),
        glob('launch/*.py')),
    ],
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='ashutosh',
    maintainer_email='ashutosh@todo.todo',
    description='Image conversion node',
    license='Apache License 2.0',
    entry_points={
        'console_scripts': [
            'image_conversion_node = image_conversion_pkg.image_conversion_node:main'
        ],
    },
)
