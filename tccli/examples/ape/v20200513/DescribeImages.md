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
        "Items": [
            {
                "ThumbUrl": "http://test.com/11.jpg",
                "Vendor": "xx",
                "Description": "xx",
                "Title": "xx",
                "ImageId": 111,
                "PreviewUrl": "http://test.com/11.jpg"
            }
        ],
        "Limit": 0,
        "HaveMore": true,
        "Offset": 30,
        "Total": 400,
        "RequestId": "xx"
    }
}
```

