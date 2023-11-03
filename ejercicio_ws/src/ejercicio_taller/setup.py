from setuptools import find_packages, setup

package_name = 'ejercicio_taller'

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
    maintainer='david',
    maintainer_email='david.villanueva.guzman@gmail.com',
    description='TODO: Package description',
    license='TODO: License declaration',
    tests_require=['pytest'],
    entry_points={
        'console_scripts': [
            'NodoRPi = ejercicio_taller.NodoRPi:main',
            'template_node = ejercicio_taller.template_node:main',
            "Nodo1 = ejercicio_taller.Nodo1:main"
        ],
    },
)
