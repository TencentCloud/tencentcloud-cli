**Example 1: 文生 3D**

通过提示词生成 3D

Input: 

```
tccli vod CreateAigcHunyuan3DTask --cli-unfold-argument  \
    --SubAppId 250000002 \
    --Prompt a warrior holding a sword \
    --KeepUV Enabled \
    --Style cyberpunk \
    --OutputConfig.StorageMode Temporary \
    --SessionId my*******Id \
    --SessionContext *********Context \
    --TasksPriority 1
```

Output: 
```
{
    "Response": {
        "TaskId": "251******-AigcHunyuan3DTask-7bf97*************afcdb0f0342fc2t",
        "RequestId": "a92d6730-19ec-4c3f-b579-44097aab0fc2"
    }
}
```

