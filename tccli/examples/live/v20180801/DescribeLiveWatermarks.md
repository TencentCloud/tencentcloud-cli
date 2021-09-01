**Example 1: 请求示例**



Input: 

```
tccli live DescribeLiveWatermarks --cli-unfold-argument ```

Output: 
```
{
    "Response": {
        "RequestId": "3c140219-cfe9-470e-b241-907877d6fb03",
        "TotalNum": 1,
        "WatermarkList": [
            {
                "WatermarkId": 123,
                "PictureUrl": "http://watermark.myqcloud.com/watermark_img_Alogo1.png",
                "XPosition": 80,
                "YPosition": 10,
                "Width": 0,
                "Height": 0,
                "WatermarkName": "logo",
                "Status": 1,
                "CreateTime": "2018-09-07T15:55:23Z"
            }
        ]
    }
}
```

