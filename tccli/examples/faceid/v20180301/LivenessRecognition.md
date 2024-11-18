**Example 1: 静默活体人脸核身成功示例**



Input: 

```
tccli faceid LivenessRecognition --cli-unfold-argument  \
    --IdCard 11204416541220243X \
    --LivenessType SILENT \
    --Name 韦小宝 \
    --VideoBase64 AAAAIGZ0eX...0tLS0tLS8=
```

Output: 
```
{
    "Response": {
        "Result": "Success",
        "Description": "成功",
        "BestFrameBase64": "/9j/4AAQSkZJRg.....s97n//2Q==",
        "BestFrameList": [
            "/9j/4AAQSk...ZpGq7an//Z"
        ],
        "Sim": 89.88,
        "RequestId": "f904f4cf-75db-4f8f-a5ec-dc4f942c7f7a"
    }
}
```

**Example 2: 数字活体人脸核身失败示例**



Input: 

```
tccli faceid LivenessRecognition --cli-unfold-argument  \
    --IdCard 11204416541220243X \
    --LivenessType LIP \
    --Name 韦小宝 \
    --VideoBase64 AAAAIGZ0eX...0tLS0tLS8= \
    --ValidateData 4903
```

Output: 
```
{
    "Response": {
        "BestFrameBase64": "/9j/4AAQSk...ZpGq7an//Z",
        "BestFrameList": [],
        "Description": "声音识别失败",
        "RequestId": "0187d319-86ac-4687-807f-7733d54ba0c0",
        "Result": "FailedOperation.LipVoiceRecognize",
        "Sim": 0
    }
}
```

