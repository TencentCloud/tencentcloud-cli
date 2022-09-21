**Example 1: 重启实例**

本示例用于重启两个实例。

Input: 

```
tccli cvm RebootInstances --cli-unfold-argument  \
    --StopType SOFT \
    --InstanceIds ins-5d8a23rs ins-r8hr2upy
```

Output: 
```
{
    "Response": {
        "RequestId": "6ef60bec-0242-43af-bb20-270359fb54a7"
    }
}
```

