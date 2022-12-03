JPEG 画像
===============

.. jinja:: image_context

    {% for size in image_sizes %}

    - {{size}} x {{size}}

      .. image:: https://kicon.musicscience37.com/KIcon{{size}}.jpg
          :target: https://kicon.musicscience37.com/KIcon{{size}}.jpg

    {% endfor %}
