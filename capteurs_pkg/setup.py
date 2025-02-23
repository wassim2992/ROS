from setuptools import find_packages, setup

package_name = 'capteurs_pkg'

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
        "capteur_temp = capteurs_pkg.capteur_temp:main",
        "capteur_humidite = capteurs_pkg.capteur_humidite:main",
        "capteur_presence = capteurs_pkg.capteur_presence:main",

    ],
},
)
