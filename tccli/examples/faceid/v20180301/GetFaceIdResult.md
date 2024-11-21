**Example 1: 获取SDK核验结果成功示例**



Input: 

```
tccli faceid GetFaceIdResult --cli-unfold-argument  \
    --FaceIdToken CE661F1A-0F1E-45BD-BE113-34C05CEA76811
```

Output: 
```
{
    "Response": {
        "BestFrameBase64": "/9j/4AAQSk...1Udr+R/9k=",
        "Description": "成功",
        "DeviceInfoLevel": null,
        "DeviceInfoTag": null,
        "Extra": "",
        "IdCard": "",
        "LivenessInfoTag": null,
        "Name": "",
        "RequestId": "13c51421-3b1d-4b40-8206-8dacedec2d32",
        "Result": "0",
        "RiskInfoTag": "",
        "Similarity": 0,
        "VideoBase64": ""
    }
}
```

**Example 2: 获取SDK核验结果人脸检测失败示例**



Input: 

```
tccli faceid GetFaceIdResult --cli-unfold-argument  \
    --FaceIdToken CE661F1A-0F1E-45BD-BE113-34C05CEA76831
```

Output: 
```
{
    "Response": {
        "BestFrameBase64": "/9j/4AAQSk...9Dl1t//9k=",
        "Description": "人脸检测失败，无法提取比对照",
        "DeviceInfoLevel": null,
        "DeviceInfoTag": null,
        "Extra": "",
        "IdCard": "",
        "LivenessInfoTag": null,
        "Name": "",
        "RequestId": "391e4084-43dd-4b03-b31c-c92a519d40bd",
        "Result": "1004",
        "RiskInfoTag": "",
        "Similarity": 0,
        "VideoBase64": "AAAAGGZ0eX...AAAAAAAAA="
    }
}
```

