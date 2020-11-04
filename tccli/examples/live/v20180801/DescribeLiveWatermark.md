**Example 1: 请求示例**



Input: 

```
tccli live DescribeLiveWatermark --cli-unfold-argument  \
    --WatermarkId 10001
```

Output: 
```
{
    "Response": {
        "Watermark": {
            "WatermarkId": 10001,
            "PictureUrl": "http://watermark.myqcloud.com/watermark_img_Alogo1.png",
            "XPosition": 80,
            "YPosition": 10,
            "Width": 0,
            "Height": 0,
            "WatermarkName": "logo",
            "Status": 1,
            "CreateTime": "2018-09-07T15:55:23Z"
        },
        "RequestId": "3c140219-cfe9-470e-b241-907877d6fb03"
    }
}
```

