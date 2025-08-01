**Example 1: 创建标准引擎资源组**

创建标准引擎资源组

Input: 

```
tccli dlc CreateStandardEngineResourceGroup --cli-unfold-argument  \
    --EngineResourceGroupName ricky \
    --DataEngineName spark_common_two \
    --AutoLaunch 1 \
    --AutoPause 1 \
    --AutoPauseTime 0 \
    --DriverCuSpec small \
    --ExecutorCuSpec small \
    --MinExecutorNums 1 \
    --MaxExecutorNums 1 \
    --IsLaunchNow 1
```

Output: 
```
{
    "Response": {
        "RequestId": "a2fa37ab-dd67-4120-b3cd-386316be0d40"
    }
}
```

