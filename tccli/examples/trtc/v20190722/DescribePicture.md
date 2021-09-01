**Example 1: 查询图片信息**



Input: 

```
tccli trtc DescribePicture --cli-unfold-argument  \
    --SdkAppId 123456 \
    --PictureId 123
```

Output: 
```
{
    "Response": {
        "Total": 2,
        "PictureInfo": [
            {
                "PictureId": 1,
                "Height": 12,
                "Width": 13,
                "XPosition": 14,
                "YPosition": 15,
                "SdkAppId": 123456
            },
            {
                "PictureId": 2,
                "Height": 22,
                "Width": 23,
                "XPosition": 24,
                "YPosition": 25,
                "SdkAppId": 123456
            }
        ],
        "RequestId": "83ca6fdd-cf4c-46a9-a577-74c3497ad3fa"
    }
}
```

