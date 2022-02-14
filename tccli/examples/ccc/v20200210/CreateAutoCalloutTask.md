**Example 1: 创建任务**



Input: 

```
tccli ccc CreateAutoCalloutTask --cli-unfold-argument  \
    --SdkAppId 1400123455 \
    --NotBefore 1642500621 \
    --Callees 008613012345678 \
    --Callers 008602012345678 \
    --IvrId 8
```

Output: 
```
{
    "Response": {
        "RequestId": "xx",
        "TaskId": 1
    }
}
```

