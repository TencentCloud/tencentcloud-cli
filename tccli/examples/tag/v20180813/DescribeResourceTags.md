**Example 1: 查询资源关联的列表**



Input: 

```
tccli tag DescribeResourceTags --cli-unfold-argument  \
    --ServiceType cvm \
    --ResourcePrefix instance \
    --ResourceRegion ap-beijing \
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
                "TagKey": "testkey",
                "TagKeyMd5": "abced",
                "TagValue": "testvalue",
                "TagValueMd5": "abced",
                "ResourceId": "ins-1234"
            }
        ],
        "RequestId": "5024400f-ae5c-4080-b3ca-f45bf9dae21a"
    }
}
```

**Example 2: 查询COS资源关联的列表**

cos的resourceId格式为bucketname-appId

Input: 

```
tccli tag DescribeResourceTags --cli-unfold-argument  \
    --ServiceType cos \
    --ResourceRegion ap-beijing \
    --ResourceId testbucket-1250000 \
    --CosResourceId 1
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
                "ServiceType": "cos",
                "TagKey": "testkey",
                "TagKeyMd5": "abced",
                "TagValue": "testvalue",
                "TagValueMd5": "abced",
                "ResourceId": "testbucket-1250000"
            }
        ],
        "RequestId": "5024400f-ae5c-4080-b3ca-f45bf9dae21a"
    }
}
```

