Propeller for Django
====================

Write Django as usual, and let ``django-propeller`` make template output into code based on Google's Material Design Standards & Bootstrap.


[![Build Status](https://travis-ci.org/tfroehlich82/django-propeller.svg?branch=master)](https://travis-ci.org/tfroehlich82/django-propeller)
![PyPI version](http://img.shields.io/pypi/v/django-propeller.svg)
![PyPI downloads](http://img.shields.io/pypi/dm/django-propeller.svg)


Requirements
------------

- Python 2.7, 3.2, 3.3, 3.4, or 3.5
- Django >= 1.10


Installation
------------

1. Install using pip:
```
    pip install django-propeller
```

2. Add to INSTALLED_APPS in your ``settings.py``:

   ```
   'django_propeller',
   ```

3. In your templates, load the ``django_propeller`` library and use the ``propeller_*`` tags:



Example template
----------------

```
    {% load propeller %}

    {# Display a form #}

    <form action="/url/to/submit/" method="post" class="form">
        {% csrf_token %}
        {% propeller_form form %}
        {% buttons %}
            <button type="submit" class="btn btn-primary">
                {% propeller_icon "star" %} Submit
            </button>
        {% endbuttons %}
    </form>
```


Documentation
-------------

The full documentation is at http://django-propeller.readthedocs.io/en/latest/


Bugs and suggestions
--------------------

If you have found a bug or if you have a request for additional functionality, please use the issue tracker on GitHub.

https://github.com/tfroehlich82/django-propeller/issues


Further Information
-------------------

Propeller: http://propeller.in/
Bootstrap: http://getbootstrap.com/
Google Material Design: https://design.google.com/


Donation
--------

[![Donation](https://www.paypalobjects.com/en_US/i/btn/btn_donateCC_LG.gif)](https://www.paypal.com/cgi-bin/webscr?cmd=_s-xclick&hosted_button_id=ARFDZCBQTWRSQ)


License
-------

You can use this under MIT License. See [LICENSE](LICENSE) file for details.


Author
------

Developed and maintained by [Thorsten Fröhlich](https://github.com/tfroehlich82),
based on the idea of django-bootstrap3 from [Dylan Verheul](https://github.com/dyve).
