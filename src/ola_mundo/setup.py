from setuptools import find_packages, setup

package_name = 'ola_mundo'

setup(
    name=package_name,
    version='0.0.0',
    packages=find_packages(exclude=['test']),
    data_files=[
        ('share/ament_index/resource_index/packages',
            ['resource/' + package_name]),
        ('share/' + package_name, ['package.xml']),
    ],
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='ana',
    maintainer_email='ana@todo.todo',
    description='pipipipopopo',
    license='CCO',
    tests_require=['pytest'],
    entry_points={
        'console_scripts': [
            "ola = ola_mundo.test:main",
        ],
    },
)
