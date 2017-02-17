from distutils.core import setup

setup(
    name='django-propeller',
    version='1.0.0',
    packages=['demo.demo', 'django_propeller', 'django_propeller.migrations', 'django_propeller.templatetags',
              'django_propeller.static'],
    url='https://github.com/tfroehlich82/django-propeller',
    license='MIT',
    author='Thorsten Froehlich',
    author_email='tfroehlich82@gmx.ch',
    description='Propeller integration with Django. Propeller is a front-end responsive framework based on Google\'s '
                'Material Design Standards & Bootstrap. http://propeller.in/index.html'
)