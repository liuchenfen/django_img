# coding=utf-8
from django.http import HttpResponse, HttpResponseBadRequest
from django import forms
from io import BytesIO
from PIL import Image, ImageDraw
from django.core.cache import cache

from django.views.decorators.http import etag

# class ImageForm(forms.Form):
#     height = forms.IntegerField(min_value=1, max_value=2000)
#     width = forms.IntegerField(min_value=1, max_value=2000)

def generate(width,height,image_format="PNG"):
    # 服务器缓存,先看是否已有缓存
    key = '{}.{}.{}'.format(width, height, image_format)
    content = cache.get(key)
    if content is None:
        image = Image.new('RGB', (width, height))
        draw = ImageDraw.Draw(image)
        text = '{}x{}'.format(width, height)
        textwidth, textheight = draw.textsize(text)
        if textwidth < width and textheight < height:
            texttop = (height - textheight) // 2
            textleft = (width - textwidth) // 2
            draw.text((textleft, texttop), text, fill=(255, 0, 0))
        content = BytesIO()
        image.save(content, image_format)
        content.seek(0)
        # #   加入缓存
        # cache.set(key,content,60 * 60)
    return content

# 浏览器缓存: etag 可以利用浏览器缓存技术
# import hashlib
# def generate_etag(request,width,height):
#     content = 'Placeholder:{0}×{1}'.format(width,height)
#     return hashlib.sha1(content.encode('utf-8')).hexdigest()
#
# @etag(generate_etag)
# def placeholder(request, width, height):
#     # 传给视图的参数都是字符串,可以利用表单验证
#     form = generate({'height': height, 'width': width})
#     if form.is_valid():
#         height = form.cleaned_data['height']
#         width = form.cleaned_data['width']
#         # 生成特定尺寸的图片
#         image = form.generate()
#         return HttpResponse(image, content_type='image/png')
#     else:
#         return HttpResponseBadRequest('Invalid Image Request')


# def generate(width,height,image_format="PNG"):
#     image=Image.new('RGB',(width,height))
#     draw=ImageDraw.Draw(image)
#     text="{}x{}".format(width,height)
#     textwidth,textheight=draw.textsize(text)
#     if textwidth<width and textheight<height:
#         texttop=(height-textheight)//2
#         textleft=(width-textwidth)//2
#         draw.text((textleft,texttop),text,fill=(255,0,0))
#
#     content = BytesIO()
#     image.save(content, image_format)
#     content.seek(0)
#     # image.show()
#     return content
# # generate(400,300)
    
    
    
    