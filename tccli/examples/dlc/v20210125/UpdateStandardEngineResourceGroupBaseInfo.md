**Example 1: 更新资源组基础配置信息**

更新资源组基础配置信息

Input: 

```
tccli dlc UpdateStandardEngineResourceGroupBaseInfo --cli-unfold-argument  \
    --EngineResourceGroupName test-rg \
    --AutoLaunch 1 \
    --AutoPause 1 \
    --AutoPauseTime 20
```

Output: 
```
{
    "Response": {
        "RequestId": "c3e5af77-11bd-4820-aa80-8a3014c4215b"
    }
}
```

