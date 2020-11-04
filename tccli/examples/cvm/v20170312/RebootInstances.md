**Example 1: 重启实例**

本示例用于重启两个实例。

Input: 

```
tccli cvm RebootInstances --cli-unfold-argument  \
    --InstanceIds ins-r8hr2upy ins-5d8a23rs\
    --ForceReboot FALSE
```

Output: 
```
{
    "Response": {
        "RequestId": "6ef60bec-0242-43af-bb20-270359fb54a7"
    }
}
```

