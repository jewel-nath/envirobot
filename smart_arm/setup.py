from setuptools import find_packages, setup
import os 
from glob import glob

package_name = 'smart_arm'

setup(
    name=package_name,
    version='0.0.0',
    packages=find_packages(exclude=['test']),
    data_files=[
        ('share/ament_index/resource_index/packages', ['resource/' + package_name]),
        ('share/' + package_name, ['package.xml']),
        (os.path.join('share', package_name, 'launch'), glob(os.path.join('launch', '*.launch.py'))),
        (os.path.join('share', package_name, 'config'), glob(os.path.join('config', '*.*'))),
        #world folder 
        (os.path.join('share', package_name, 'worlds'), glob(os.path.join('worlds', '*.world'))),
        #description folder
        (os.path.join('share', package_name, 'description'), glob(os.path.join('description', '*.xacro'))),
        #description/meshes folder 
        (os.path.join('share', package_name, 'description','meshes'), glob(os.path.join('description','meshes', '*.stl'))),
        (os.path.join('share', package_name, 'description','meshes'), glob(os.path.join('description','meshes', '*.dae'))),

    ],
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='jewel',
    maintainer_email='devjewel01@stud.cou.ac.bd',
    description='TODO: Package description',
    license='TODO: License declaration',
    tests_require=['pytest'],
    entry_points={
        'console_scripts': [
        ],
    },
)
