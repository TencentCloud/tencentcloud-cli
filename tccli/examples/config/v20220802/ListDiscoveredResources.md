**Example 1: 获取资源列表**



Input: 

```
tccli config ListDiscoveredResources --cli-unfold-argument  \
    --OrderType xx \
    --NextToken xx \
    --MaxResults 1 \
    --Filters.0.Values xx \
    --Filters.0.Name xx \
    --Tags.0.TagKey xx \
    --Tags.0.TagValue xx
```

Output: 
```
{
    "Response": {
        "Items": [
            {
                "ResourceStatus": "xx",
                "Tags": [
                    {
                        "TagKey": "xx",
                        "TagValue": "xx"
                    }
                ],
                "ResourceType": "xx",
                "ResourceId": "xx",
                "ResourceCreateTime": 1,
                "ResourceRegion": "xx",
                "ResourceName": "xx",
                "ResourceZone": "xx",
                "ResourceDelete": 1,
                "ComplianceResult": "xx"
            }
        ],
        "NextToken": "xx",
        "RequestId": "xx"
    }
}
```

