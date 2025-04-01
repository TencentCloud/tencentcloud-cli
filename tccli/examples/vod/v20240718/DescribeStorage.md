**Example 1: 分页查询专业版应用存储信息**

按照创建时间倒序，分页查询专业版应用的存储信息。

Input: 

```
tccli vod DescribeStorage --cli-unfold-argument  \
    --SubAppId 1234567890 \
    --SortBy.Field CreateTime \
    --SortBy.Order Desc \
    --Offset 0 \
    --Limit 20
```

Output: 
```
{
    "Response": {
        "TotalCount": 2,
        "StorageInfoSet": [
            {
                "BucketId": "bucketId123demo",
                "CreateTime": "2024-07-18T00:00:00+00:00",
                "InternetAccessDomain": "example123.vodpro.ap-guangzhou.eovod.com",
                "InternetAccessDomainStatus": "DEPLOYING",
                "StorageName": "my-storage",
                "StorageRegion": "ap-guangzhou"
            },
            {
                "BucketId": "bucketId456demo",
                "CreateTime": "2024-07-17T00:00:00+00:00",
                "InternetAccessDomain": "example456.vodpro.ap-guangzhou.eovod.com",
                "InternetAccessDomainStatus": "ONLINE",
                "StorageName": "my-storage2",
                "StorageRegion": "ap-shanghai"
            }
        ],
        "RequestId": "af4b9a1e-8df1-demo-reqid-ac6364f13e69"
    }
}
```

**Example 2: 按照存储桶 ID 查询专业版应用的存储信息**

添加查询过滤器 Filter，按照存储桶 ID 过滤查询存储桶信息。

Input: 

```
tccli vod DescribeStorage --cli-unfold-argument  \
    --SubAppId 1234567890 \
    --Filters.0.Name BucketId \
    --Filters.0.Values bucketId123demo
```

Output: 
```
{
    "Response": {
        "TotalCount": 1,
        "StorageInfoSet": [
            {
                "BucketId": "bucketId123demo",
                "CreateTime": "2024-07-18T00:00:00+00:00",
                "InternetAccessDomain": "example123.vodpro.ap-guangzhou.eovod.com",
                "InternetAccessDomainStatus": "DEPLOYING",
                "StorageName": "my-storage",
                "StorageRegion": "ap-guangzhou"
            }
        ],
        "RequestId": "bf5c72d0-5b34-demo-reqid-4b5a2d7b4c68"
    }
}
```

