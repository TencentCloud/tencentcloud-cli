**Example 1: 暂停指定资源组**

暂停指定资源组

Input: 

```
tccli dlc PauseStandardEngineResourceGroups --cli-unfold-argument  \
    --EngineResourceGroupNames test-session
```

Output: 
```
{
    "Response": {
        "OperateEngineResourceGroupFailMessages": [],
        "RequestId": "b2a83c9e-ddf8-43b5-a308-3d0c743976d4"
    }
}
```

