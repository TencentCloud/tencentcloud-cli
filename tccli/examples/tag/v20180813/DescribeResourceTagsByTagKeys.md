**Example 1: 根据标签键获取资源标签**

根据标签键获取资源标签

Input: 

```
tccli tag DescribeResourceTagsByTagKeys --cli-unfold-argument  \
    --ServiceType cvm \
    --ResourcePrefix instance \
    --ResourceRegion ap-beijing \
    --ResourceIds ins-1234 \
    --TagKeys abc edf
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
                "ResourceId": "ins-asdfsadf",
                "TagKeyValues": [
                    {
                        "TagKey": "abc",
                        "TagValue": "edf"
                    }
                ]
            }
        ],
        "RequestId": "5024400f-ae5c-4080-b3ca-f45bf9dae21a"
    }
}
```

