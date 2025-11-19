**Example 1: 更新资源组资源配置**

更新资源组资源配置

Input: 

```
tccli dlc UpdateStandardEngineResourceGroupResourceInfo --cli-unfold-argument  \
    --EngineResourceGroupName test-rg \
    --DriverCuSpec small \
    --ExecutorCuSpec small \
    --MinExecutorNums 1 \
    --MaxExecutorNums 1 \
    --IsEffectiveNow 1
```

Output: 
```
{
    "Response": {
        "RequestId": "b12eb63a-37d1-4b9c-ac9a-8995ccc89b58"
    }
}
```

