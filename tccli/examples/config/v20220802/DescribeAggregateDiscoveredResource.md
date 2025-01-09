**Example 1: 获取资源详情**

获取资源详情

Input: 

```
tccli config DescribeAggregateDiscoveredResource --cli-unfold-argument  \
    --ResourceOwnerId 1 \
    --AccountGroupId ad-234234234234 \
    --ResourceId adad-adasd-1307051190 \
    --ResourceRegion ap-nanjing \
    --ResourceType QCS::COS::Bucket
```

Output: 
```
{
    "Response": {
        "RequestId": "701285ae-1e8e-4189-9d7a-e9dec4fadae6",
        "Configuration": "{\"Acl\":[{\"Grantee\":null,\"Permission\":\"FULL_CONTROL\"}],\"Url\":\"https://adad-adasd-1307051190.cos.ap-nanjing.myqcloud.com\",\"Version\":\"\",\"Log\":{\"TargetBucket\":\"\",\"TargetPrefix\":\"\"},\"Encryption\":null}",
        "ResourceCreateTime": "2022-09-01 10:36:51",
        "ResourceId": "adad-adasd-1307051190",
        "ResourceName": "adad-adasd-1307051190",
        "ResourceRegion": "ap-nanjing",
        "ResourceType": "QCS::COS::Bucket",
        "ResourceZone": "global",
        "Tags": [
            {
                "TagKey": "asd",
                "TagValue": "asd"
            }
        ],
        "UpdateTime": "2022-11-16 11:20:00"
    }
}
```

