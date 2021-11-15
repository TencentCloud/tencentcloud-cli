**Example 1: 创建资源示例**



Input: 

```
tccli oceanus CreateResource --cli-unfold-argument  \
    --Name testjar \
    --ResourceType 1 \
    --FolderId folder-xxxxx \
    --ResourceLoc.StorageType 1 \
    --ResourceLoc.Param.Bucket oceanus-online-resource-xxxxx \
    --ResourceLoc.Param.Path 123456/10000534/testjar/xxx
```

Output: 
```
{
    "Response": {
        "RequestId": "d7b76d5e-ad7d-4abd-b3b2-43b96dd08d16",
        "ResourceId": "resource-jj4fx50r",
        "Version": 1
    }
}
```

