**Example 1: 获取资源列表**



Input: 

```
tccli config ListDiscoveredResources --cli-unfold-argument  \
    --OrderType desc \
    --NextToken C3IptlTj6hTlW0WKVO3NI \
    --MaxResults 10 \
    --Filters.0.Values ins-234234 \
    --Filters.0.Name resourceName \
    --Tags.0.TagKey 开发部 \
    --Tags.0.TagValue 运营部
```

Output: 
```
{
    "Response": {
        "Items": [
            {
                "ResourceStatus": "Running",
                "Tags": [
                    {
                        "TagKey": "开发部",
                        "TagValue": "运营部"
                    }
                ],
                "ResourceType": "cvm",
                "ResourceId": "ins-234er",
                "ResourceCreateTime": "2022-10-10 12:56:37",
                "ResourceRegion": "ap-guangzhou",
                "ResourceName": "云服务器",
                "ResourceZone": "ap-guangzhou-1",
                "ResourceDelete": 1,
                "ComplianceResult": "COMPLIANT"
            }
        ],
        "NextToken": "C3IptlTj6hTlW0WKVO3NI",
        "RequestId": "4006b9ea-9b33-4b80-8496-6917c900b122"
    }
}
```

