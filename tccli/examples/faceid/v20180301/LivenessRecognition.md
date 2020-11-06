**Example 1: 静默活体人脸核身**



Input: 

```
tccli faceid LivenessRecognition --cli-unfold-argument  \
    --IdCard 11204416541220243X \
    --Name 韦小宝 \
    --VideoBase64 <VideoBase64> \
    --LivenessType SILENT
```

Output: 
```
{
    "Response": {
        "Result": "Success",
        "Description": "成功",
        "BestFrameBase64": "<Imagebase64>",
        "Sim": "89.88",
        "RequestId": "f904f4cf-75db-4f8f-a5ec-dc4f942c7f7a"
    }
}
```

