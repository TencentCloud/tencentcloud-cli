**Example 1: 根据关键字搜索图片**



Input: 

```
tccli ape DescribeImages --cli-unfold-argument  \
    --Keyword 关键字 \
    --Offset 0 \
    --Limit 30
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

