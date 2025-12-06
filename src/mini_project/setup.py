from setuptools import find_packages, setup

package_name = 'mini_project'

setup(
    name=package_name,
    version='0.0.0',
    packages=find_packages(exclude=['test']),
    data_files=[
        ('share/ament_index/resource_index/packages',
            ['resource/' + package_name]),
        ('share/' + package_name, ['package.xml']),
        ('share/' + package_name + '/launch', ['launch/project.launch.py']),
    ],
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='yahia',
    maintainer_email='yahiaboukharrata092@gmail.com',
    description='TODO: Package description',
    license='Apache-2.0',
    extras_require={
        'test': [
            'pytest',
        ],
    },
    entry_points={
        'console_scripts': [
            "talker = mini_project.publisher:main",
            "listener = mini_project.subscriber:main",
        ],
    },
)
