**Example 1: 关闭实例**

本示例用于关闭两个实例。

Input: 

```
tccli cvm StopInstances --cli-unfold-argument  \
    --InstanceIds ins-r8hr2upy ins-5d8a23rs \
    --ForceStop FALSE
```

Output: 
```
{
    "Response": {
        "RequestId": "6ef60bec-0242-43af-bb20-270359fb54a7"
    }
}
```

