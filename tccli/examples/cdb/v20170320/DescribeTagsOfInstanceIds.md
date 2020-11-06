**Example 1: 获取实例标签信息**

获取实例标签信息

Input: 

```
tccli cdb DescribeTagsOfInstanceIds --cli-unfold-argument  \
    --InstanceIds cdb-uns231ns \
    --Offset 0 \
    --Limit 10
```

Output: 
```
{
    "Response": {
        "RequestId": "6EF60BEC-0242-43AF-BB20-270359FB54A7",
        "Offset": 0,
        "Limit": 10,
        "Rows": [
            {
                "InstanceId": "cdb-uns231ns",
                "Tags": [
                    {
                        "TagKey": "test",
                        "TagValue": "1231"
                    }
                ]
            }
        ]
    }
}
```

