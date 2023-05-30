**Example 1: 请求示例**

更新水印

Input: 

```
tccli live UpdateLiveWatermark --cli-unfold-argument  \
    --WatermarkId 123 \
    --PictureUrl http://watermark-10005041.cos.myqcloud.com/1251830167/watermark_img_Alogo.png \
    --XPosition 80 \
    --YPosition 10 \
    --WatermarkName logo
```

Output: 
```
{
    "Response": {
        "RequestId": "3c140219-cfe9-470e-b241-907877d6fb03"
    }
}
```

