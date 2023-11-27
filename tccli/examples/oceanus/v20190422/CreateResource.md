**Example 1: 创建依赖**

创建依赖

Input: 

```
tccli oceanus CreateResource --cli-unfold-argument  \
    --ResourceLoc.StorageType 1 \
    --ResourceLoc.Param.Bucket oceanus-online-resource01-gz-1257058918 \
    --ResourceLoc.Param.Path 1257058945/100006386216/upload/20231120142441/flink-hello-world-1.0.0-jar-with-dependencies.jar \
    --ResourceLoc.Param.Region ap-guangzhou \
    --Remark test \
    --Name flink-hello-world-1.0.0-jar-with-dependencies.jar \
    --ResourceType 1 \
    --WorkSpaceId space-53rqk422
```

Output: 
```
{
    "Response": {
        "RequestId": "1a7f54d8-fbfa-4367-a572-219c46b18058",
        "ResourceId": "resource-gk2iv5z5",
        "Version": 1
    }
}
```

