**Example 1: 查询图片信息**



Input: 

```
tccli trtc DescribePicture --cli-unfold-argument  \
    --SdkAppId 140000001 \
    --PictureId 100861
```

Output: 
```
{
    "Response": {
        "Total": 2,
        "PictureInfo": [
            {
                "PictureId": 100861,
                "Height": 120,
                "Width": 113,
                "XPosition": 124,
                "YPosition": 150,
                "SdkAppId": 140000001
            }
        ],
        "RequestId": "83ca6fdd-cf4c-46a9-a577-74c3497ad3fa"
    }
}
```

