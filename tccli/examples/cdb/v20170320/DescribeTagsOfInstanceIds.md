**Example 1: Obtaining the instance tag information**

This example shows you how to obtain the instance tag information.

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

