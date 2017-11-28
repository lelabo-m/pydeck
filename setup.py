from setuptools import setup

setup(name='genericdeck',
    version='1.0.0',
    description='Generic deck system for cards, dominos, etc.',
    author='Marc Le Labourier',
    author_email='marc.lelabourier@gmail.com',
    license='NONE',
    packages=[
        'genericdeck',
        'genericdeck/generic',
    ],
    package_dir={
        'genericdeck': 'src',
        'genericdeck/generic': 'src/generic',
    },
    zip_safe=False)
