**Example 1: 创建资源**



Input: 

```
tccli wedata CreateResourceFile --cli-unfold-argument  \
    --ProjectId 1460947xxxxxxxx6 \
    --ResourceName api_list_dev.csv \
    --BucketName 1219-agent-13xxx9 \
    --CosRegion ap-beijing \
    --ParentFolderPath /qxxxxx/q2 \
    --ResourceFile None \
    --BundleId 253 \
    --BundleInfo wedata
```

Output: 
```
{
    "Response": {
        "Data": {
            "ResourceId": "5851e178-19c8-4ccf-9719-fda1e6b0b8eb"
        },
        "RequestId": "9b8d1e11-93db-4d27-9e88-3cdb7559ebe1"
    }
}
```

