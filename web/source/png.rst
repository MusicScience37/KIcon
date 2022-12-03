PNG 画像
===============

.. contents:: Contents
    :local:

背景が透明の画像
-----------------------

.. jinja:: image_context

    {% for size in image_sizes %}

    - {{size}} x {{size}}

      .. image:: https://kicon.musicscience37.com/KIcon{{size}}.png
          :target: https://kicon.musicscience37.com/KIcon{{size}}.png

    {% endfor %}

背景が白の画像
-----------------------

.. jinja:: image_context

    {% for size in image_sizes %}

    - {{size}} x {{size}}

      .. image:: https://kicon.musicscience37.com/KIcon{{size}}white.png
          :target: https://kicon.musicscience37.com/KIcon{{size}}white.png

    {% endfor %}
