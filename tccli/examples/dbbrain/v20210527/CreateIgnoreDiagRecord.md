**Example 1: 忽略CpuUsage诊断类型**

忽略诊断类型

Input: 

```
tccli dbbrain CreateIgnoreDiagRecord --cli-unfold-argument  \
    --InstanceId cdb-lvgh1oyv \
    --Product mysql \
    --DiagItem CpuUsage \
    --Status 2
```

Output: 
```
{
    "Response": {
        "RequestId": "a1a04f16-3a03-46c4-a80f-41df480c28b0"
    }
}
```

