**Example 1: 创建依赖版本**

创建依赖版本

Input: 

```
tccli oceanus CreateResourceConfig --cli-unfold-argument  \
    --ResourceId resource-qreuon9y \
    --ResourceLoc.StorageType 1 \
    --ResourceLoc.Param.Bucket oceanus-online-resource01-gz-1257058918 \
    --ResourceLoc.Param.Path 1257058945/100006386216/upload/20231120150319/flink-hello-world-1.0.0.jar \
    --ResourceLoc.Param.Region ap-guangzhou \
    --Remark test \
    --WorkSpaceId space-53rqk422
```

Output: 
```
{
    "Response": {
        "RequestId": "65812cf1-22bb-4ecd-89bb-01fe5a12ffb2",
        "Version": 3
    }
}
```

