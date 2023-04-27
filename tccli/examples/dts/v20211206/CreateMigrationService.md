**Example 1: 购买迁移任务**

购买迁移任务

Input: 

```
tccli dts CreateMigrationService --cli-unfold-argument  \
    --SrcDatabaseType mysql \
    --DstDatabaseType mysql \
    --InstanceClass xlarge \
    --SrcRegion ap-guangzhou \
    --DstRegion ap-guangzhou \
    --Tags.0.TagKey testkey \
    --Tags.0.TagValue testvalue
```

Output: 
```
{
    "Response": {
        "JobIds": [
            "dts-1ewjspuw"
        ],
        "RequestId": "ac300ff0-00f2-11ed-b005-4930e69d89c2"
    }
}
```

