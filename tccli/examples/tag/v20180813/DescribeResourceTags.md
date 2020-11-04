**Example 1: 通过标签查询资源列表**



Input: 

```
tccli tag DescribeResourceTags --cli-unfold-argument  \
    --ServiceType cvm\
    --ResourcePrefix instance\
    --ResourceRegion ap-beijing\
    --ResourceId ins-1234
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
                "ServiceType": "cvm",
                "TagKey": "instance",
                "TagKeyMd5": "abced",
                "TagValue": "ins-asdfsadf",
                "TagValueMd5": "abced",
                "ResourceId": "ins-asdfsadf"
            }
        ],
        "RequestId": "5024400f-ae5c-4080-b3ca-f45bf9dae21a"
    }
}
```

