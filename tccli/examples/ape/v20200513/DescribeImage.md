**Example 1: 查询图片详情**

根据图片id查询图片详细信息

Input: 

```
tccli ape DescribeImage --cli-unfold-argument  \
    --ImageId 4723211
```

Output: 
```
{
    "Response": {
        "Description": "early,morning,sky,with,colors,from,deep,blue,to,orange,",
        "Height": 683,
        "ImageFormat": "jpg",
        "ImageId": 15053134,
        "ImageSenseType": "photo",
        "Keywords": "背景,漂亮的,美丽,蓝色,明亮,云,云景,多云的,颜色,多姿多彩,黎明时分,深度,戏剧性的,黄昏,地平线,分层,灯,早上,天然的,自然界,夜晚,海洋,桔黄色的,橙色的天空,橙色日出,橙色的日落,红色,浪漫的,景观,场景,风景名胜区,天空,天空景观,天空景观,地层,层状结构,夏天,太阳,阳光,日出,日落,充满活力,视图,vista,黄色",
        "LayeredGalleryId": 2,
        "Marshals": [],
        "Orientation": "horizontal",
        "PreviewUrl": "https://xxxxxxx024.jpg?imageMogr2/thumbnail/600x600/interlace/0",
        "RequestId": "s1612237208109201750",
        "ThumbUrl": "https://xxxxxx.jpg?imageMogr2/thumbnail/300x300/interlace/0",
        "Title": "morning,sky",
        "Vendor": "北京xx公司",
        "Width": 1024
    }
}
```

