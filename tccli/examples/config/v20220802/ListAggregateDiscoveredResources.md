**Example 1: 获取资源列表**

获取资源列表

Input: 

```
tccli config ListAggregateDiscoveredResources --cli-unfold-argument  \
    --AccountGroupId ca-sdfsdfsdf \
    --OrderType DESC \
    --Tags.0.TagKey TAG1 \
    --Tags.0.TagValue TAG3 \
    --MaxResults 1 \
    --Filters.0.Values CVM \
    --Filters.0.Name resourceType \
    --NextToken sdfsdfsdf456457rsf
```

Output: 
```
{
    "Response": {
        "Items": [
            {
                "ResourceStatus": "1",
                "ResourceOwnerId": 1,
                "Tags": [
                    {
                        "TagKey": "TAG2",
                        "TagValue": "33ATG5"
                    }
                ],
                "ResourceType": "cvm",
                "ResourceId": "ins-324234",
                "ResourceCreateTime": "234234234234",
                "ResourceRegion": "ap-hangzhou",
                "ResourceName": "服务器",
                "ResourceZone": "ap-guanghzou",
                "ResourceDelete": 1,
                "ComplianceResult": "COMPLIANCE"
            }
        ],
        "NextToken": "0f6ac54682ee49d5b0",
        "RequestId": "3d105d8-5820-434f-9fac-76f92"
    }
}
```

