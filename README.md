# Haishoku

> `haishoku` is a JP word, it means palette in English.

Haishoku is a development tool for grabbing the dominant color or representative color palette from an image, it depends on `Python3` and `Pillow`.

### Feature

1. Grab the `dominant color` from a image.

2. Grab the representative `color palette` from a image.

3. From `v1.1.4`, Haishoku could load a image from remote url. 

### Demo
![demo](http://orhcxc3kd.bkt.clouddn.com/haishoku.png)

( original image's source: dribbble )

### Installation

```shell
pip3 install haishoku
```

or maybe you should use

```shell
python3 -m pip install haishoku
```

### Api

#### • loadHaishoku( image )

```python
from haishoku.haishoku import Haishoku
haishoku = Haishoku.loadHaishoku(image)
```

it will return a Haishoku instance, and you can use `haishoku.dominant` and `haishoku.palette` to get the image's dominant color and color palette

> Also, you can use more immediately api to get them or show them temporarily, just like below:

#### • getDominant( image )

```python
from haishoku.haishoku import Haishoku
dominant = Haishoku.getDominant(image)
```

returns: (R, G, B) `tuple`

#### • showDominant( image )

```python
from haishoku.haishoku import Haishoku
Haishoku.showDominant( image )
```

it will open a temporary image to show the dominant color.

#### • getPalette( image )

```python
from haishoku.haishoku import Haishoku
palette = Haishoku.getPalette( image )
```

returns: [(percentage, (R, G, B)), (percentage, (R, G, B)), ...] `Array` length <= 8

#### • showPalette( image )

```python
from haishoku.haishoku import Haishoku
Haishoku.showPalette( image )
```

This method now saves the image of the palette as a .PNG, instead of displaying a temporary .BMP image.<br/> The generated .PNG can be accessed outside of the package like so:
```python
from haishoku.haishoku import Haishoku
import haishoku.haillow

#generates the palette
Haishoku.showPalette(comment.submission.url)

palette_image = haishoku.haillow.image_name
```


### 中文文档

 [中文文档](docs/document_zh.md)


