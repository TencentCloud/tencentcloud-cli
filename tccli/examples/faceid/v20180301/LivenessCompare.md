**Example 1: 静默活体人脸比对成功示例**



Input: 

```
tccli faceid LivenessCompare --cli-unfold-argument  \
    --LivenessType SILENT \
    --ImageBase64 /9j/4AAQSk...GArFYH/9k= \
    --VideoBase64 AAAAIGZ0eX...cBQCKAowc=
```

Output: 
```
{
    "Response": {
        "Result": "Success",
        "Description": "成功",
        "BestFrameBase64": "/9j/4AAQSk...W8+nU//9k=",
        "BestFrameList": [
            "/9j/4AAQSk...px72+8/9k="
        ],
        "Sim": 89.88,
        "RequestId": "f904f4cf-75db-4f8f-a5ec-dc4f942c7f7a"
    }
}
```

**Example 2: 静默活体人脸比对失败示例**



Input: 

```
tccli faceid LivenessCompare --cli-unfold-argument  \
    --LivenessType SILENT \
    --ImageBase64 /9j/4AAQSk...GArFYH/9k= \
    --VideoBase64 AAAAIGZ0eX...cBQCKAowc=
```

Output: 
```
{
    "Response": {
        "BestFrameBase64": "/9j/4AAQSk...RgkelAH//Z",
        "BestFrameList": [],
        "Description": "实人检测失败",
        "RequestId": "09fe2045-af63-43d5-8d7a-d9f7834ca62e",
        "Result": "FailedOperation.SilentDetectFail",
        "Sim": 0
    }
}
```

