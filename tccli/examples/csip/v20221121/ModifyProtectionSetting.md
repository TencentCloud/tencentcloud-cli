**Example 1: 示例**



Input: 

```
tccli csip ModifyProtectionSetting --cli-unfold-argument  \
    --AssetType CWP \
    --Config.0.QUUID  \
    --Config.0.Enable 0 \
    --Config.0.VulDefEnable 0 \
    --Config.0.VulDefMode 0 \
    --Config.0.VulDefAction 0 \
    --Config.0.MemShellDefEnable 0 \
    --Config.0.PerformanceLimit 0 \
    --Config.0.PerformanceLimitCpu 0 \
    --Config.0.PerformanceLimitMem 0 \
    --Config.0.PerformanceLimitMemAmount 0 \
    --Config.0.SafeInject 0
```

Output: 
```
{
    "Response": {
        "RequestId": "00780acf-7f35-4717-b319-759b3ac5bed6"
    }
}
```

