**Example 1: 活体检测 [前往调试工具](https://console.cloud.tencent.com/api/explorer?Product=faceid&Version=2018-03-01&Action=Liveness&SignVersion=)**



Input: 

```
tccli faceid Liveness --cli-unfold-argument  \
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
        "RequestId": "f904f4cf-75db-4f8f-a5ec-dc4f942c7f7a"
    }
}
```

