**Example 1: 创建资源配置示例**



Input: 

```
tccli oceanus CreateResourceConfig --cli-unfold-argument  \
    --ResourceId resource-jj3fx50f \
    --ResourceLoc.StorageType 1 \
    --ResourceLoc.Param.Bucket oceanus-online-resource-xxxxx \
    --ResourceLoc.Param.Path 123456/10000534/testjar/xxx
```

Output: 
```
{
    "Response": {
        "Version": 15,
        "RequestId": "5d5a201f-0a3d-485f-a82f-3c73ccca348a"
    }
}
```

