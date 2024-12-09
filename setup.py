from setuptools import find_packages, setup
import os
from glob import glob

package_name = 'mrs_hudson'

setup(
    name=package_name,
    version='0.0.0',
    packages=find_packages(exclude=['test']),
    data_files=[
        ('share/ament_index/resource_index/packages',
            ['resource/' + package_name]),
        ('share/' + package_name, ['package.xml']),
        (os.path.join('share', package_name, 'launch'), glob(os.path.join('launch', 'mrs_hudson_empty_world.launch.py'))),
        (os.path.join('share', package_name, 'launch'), glob(os.path.join('launch', 'mrs_hudson_gazebo_rviz.launch.py'))),
        (os.path.join('share', package_name, 'models'), glob(os.path.join('models', 'mrs_hudson.urdf'))),
        (os.path.join('share', package_name, 'config'), glob(os.path.join('config', 'mrs_hudson.rviz'))),
        (os.path.join('share', package_name, 'worlds'), glob(os.path.join('worlds', 'mrs_hudson.sdf'))),
        (os.path.join('share', package_name, 'launch'), glob(os.path.join('launch', 'mrs_hudson_world.launch.py'))),
        (os.path.join('share', package_name, 'worlds'), glob(os.path.join('worlds', 'mrs_hudson_arena.sdf'))),
        (os.path.join('share', package_name, 'launch'), glob(os.path.join('launch', 'maze_aruco.launch.py'))),
        (os.path.join('share', package_name, 'worlds'), glob(os.path.join('worlds', 'maze_aruco.sdf'))),       
    ],
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='saurabh42',
    maintainer_email='saurabh42@todo.todo',
    description='TODO: Package description',
    license='TODO: License declaration',
    tests_require=['pytest'],
    entry_points={
        'console_scripts': ['vel_pub='+package_name+'.vel_pub:main',
        		    'mrs_hudson_teleop='+package_name+'.mrs_hudson_teleop:main',
                    'detect_marker='+package_name+'.detect_marker:main',
                    'display_camera='+package_name+'.display_camera:main',
        ],
    },
)
