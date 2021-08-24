**Example 1: 获取结果成功时**



Input: 

```
tccli faceid GetFaceIdResult --cli-unfold-argument  \
    --FaceIdToken CE661F1A-0F1E-45BD-BE13-34C05CEA7681
```

Output: 
```
{
    "Response": {
        "Result": "0",
        "Description": "成功",
        "IdCard": "23232323232",
        "Name": "王五",
        "Similarity": 97.7,
        "RequestId": "0f96cf39-a183-485c-ab29-8427ab81f9ae",
        "Extra": "xx",
        "VideoBase64": "xx",
        "BestFrameBase64": "xx",
        "DeviceInfoTag": "5007_1005",
        "RiskInfoTag": "02"
    }
}
```

