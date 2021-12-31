**Example 1: 商品识别-微信识物版接口调用成功**



Input: 

```
tccli tiia DetectProductBeta --cli-unfold-argument  \
    --ImageUrl https://test.jpg
```

Output: 
```
{
    "Response": {
        "RegionDetected": [
            {
                "Category": "家电数码",
                "CategoryScore": 0.894864857197,
                "Location": {
                    "XMin": 175,
                    "YMin": 12,
                    "XMax": 401,
                    "YMax": 376
                }
            }
        ],
        "ProductInfo": {
            "FindSKU": 1,
            "Location": {
                "XMin": 175,
                "YMin": 12,
                "XMax": 401,
                "YMax": 376
            },
            "Name": "手机",
            "Brand": "iphone",
            "Price": "￥7299",
            "ProductCategory": "家电数码",
            "Score": 0.544267654419,
            "Image": "https://wxamusic.wx.qq.com/wxasr/getminipic/MAnWZ-KslXfAMK4k0dIDv4lfYZQsAPG8r4MKYPL3fI1yDgRjXI68eyE2krz6ku0j?media-id=MAnWZ-KslXfAMK4k0dIDv4lfYZQsAPG8r4MKYPL3fI1yDgRjXI68eyE2krz6ku0j&appid=wx91d27dbf599dff74",
            "LemmaInfoList": []
        },
        "ProductInfoList": [
            {
                "FindSKU": 1,
                "Location": {
                    "XMin": 175,
                    "YMin": 12,
                    "XMax": 401,
                    "YMax": 376
                },
                "Name": "手机",
                "Brand": "iphone",
                "Price": "￥7299",
                "ProductCategory": "家电数码",
                "Score": 0.544267654419,
                "Image": "https://wxamusic.wx.qq.com/wxasr/getminipic/MAnWZ-KslXfAMK4k0dIDv4lfYZQsAPG8r4MKYPL3fI1yDgRjXI68eyE2krz6ku0j?media-id=MAnWZ-KslXfAMK4k0dIDv4lfYZQsAPG8r4MKYPL3fI1yDgRjXI68eyE2krz6ku0j&appid=wx91d27dbf599dff74",
                "LemmaInfoList": []
            }
        ],
        "RequestId": "2054720d-0c93-4028-9843-8fb9114ce2e2"
    }
}
```

