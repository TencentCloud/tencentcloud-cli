**Example 1: 通过标签查询资源列表**



Input: 

```
tccli tag DescribeResourcesByTags --cli-unfold-argument  \
    --ServiceType cvm \
    --ResourcePrefix instance \
    --ResourceRegion ap-beijing \
    --ResourceId ins-1234 \
    --TagFilters.0.TagKey key1
```

Output: 
```
{
    "Response": {
        "TotalCount": 1,
        "Offset": 0,
        "Limit": 15,
        "Rows": [
            {
                "ResourceRegion": "ap-guangzhou",
                "ServiceType": "cvm",
                "ResourcePrefix": "instance",
                "ResourceId": "ins-1234",
                "Tags": [
                    {
                        "TagKey": "key1",
                        "TagValue": "value1"
                    }
                ]
            }
        ],
        "RequestId": "5024400f-ae5c-4080-b3ca-f45bf9dae21a"
    }
}
```

