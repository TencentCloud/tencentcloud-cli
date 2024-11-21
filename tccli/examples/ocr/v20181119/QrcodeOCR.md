**Example 1: QrcodeOCR调用**

二维码和条形码识别  [前往调试工具](https://console.cloud.tencent.com/api/explorer?Product=ocr&Version=2018-11-19&Action=QrcodeOCR)

Input: 

```
tccli ocr QrcodeOCR --cli-unfold-argument  \
    --ImageUrl https://ocr-demo-1254418846.cos.ap-guangzhou.myqcloud.com/general/QrcodeOCR/QrcodeOCR1.jpg
```

Output: 
```
{
    "Response": {
        "CodeResults": [
            {
                "Position": {
                    "LeftBottom": {
                        "X": 161,
                        "Y": 640
                    },
                    "LeftTop": {
                        "X": 161,
                        "Y": 158
                    },
                    "RightBottom": {
                        "X": 638,
                        "Y": 640
                    },
                    "RightTop": {
                        "X": 638,
                        "Y": 158
                    }
                },
                "TypeName": "QR_CODE",
                "Url": "http://weixin.qq.com/r/LBNqcsHEhpz5rYUR90Y_"
            }
        ],
        "ImgSize": {
            "High": 800,
            "Wide": 800
        },
        "RequestId": "0cf283f2-b8f8-4d4c-b383-8f56740cc631"
    }
}
```

