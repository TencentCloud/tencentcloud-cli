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
        "Extra": "",
        "VideoBase64": "",
        "BestFrameBase64": "",
        "DeviceInfoTag": "01",
        "RiskInfoTag": "02",
        "LivenessInfoTag": "01",
        "DeviceInfoLevel": "1"
    }
}
```

