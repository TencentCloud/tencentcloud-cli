**Example 1: 静默活体人脸比对**



Input: 

```
tccli faceid LivenessCompare --cli-unfold-argument  \
    --LivenessType SILENT \
    --ImageBase64 <ImageBase64> \
    --VideoBase64 <VideoBase64>
```

Output: 
```
{
    "Response": {
        "Result": "Success",
        "Description": "成功",
        "BestFrameBase64": "Imagebase64",
        "BestFrameList": [
            "Imagebase64"
        ],
        "Sim": 89.88,
        "RequestId": "f904f4cf-75db-4f8f-a5ec-dc4f942c7f7a"
    }
}
```

