from setuptools import find_packages, setup

package_name = 'servclient'

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
    maintainer='bogoss',
    maintainer_email='bogoss@todo.todo',
    description='TODO: Package description',
    license='TODO: License declaration',
    tests_require=['pytest'],
    entry_points={
    'console_scripts': [
        'temperature_server = servclient.temperature_server:main',
        'temperature_client = servclient.temperature_client:main',
    ],
},

)
