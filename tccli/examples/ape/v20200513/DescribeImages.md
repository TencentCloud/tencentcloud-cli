**Example 1: 根据关键字搜索图片**



Input: 

```
tccli ape DescribeImages --cli-unfold-argument  \
    --Orientation horizontal \
    --Keyword 关键字 \
    --LayeredGalleryIds 0 \
    --Limit 0 \
    --Offset 0 \
    --ImageSenseType 插画
```

Output: 
```
{
    "Response": {
        "HaveMore": true,
        "Items": [
            {
                "Description": "天空",
                "Height": 933,
                "ImageId": 9100082,
                "Keywords": "天空，明亮，光，天空，云，蓝色，背景，云，白色，性质，光，天气，美丽，夏天，美容，颜色，天，空间，气候，空气，视图，种，阳光，高，积云，晴朗，多云，晴朗，环境，阳光，蓬松，明亮，天堂",
                "PreviewUrl": "http://test.com/11.jpg",
                "ThumbUrl": "http://test.com/11.jpg",
                "Title": "天空",
                "Vendor": "北京易维视网络科技有限公司",
                "Width": 1400
            }
        ],
        "Limit": 1,
        "Offset": 0,
        "RequestId": "s1612255055113051093",
        "Total": 9999
    }
}
```

