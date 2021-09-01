**Example 1: 获取日志集列表**



Input: 

```
tccli cls DescribeLogsets --cli-unfold-argument  \
    --Offset 0 \
    --Limit 1
```

Output: 
```
{
    "Response": {
        "TotalCount": 0,
        "RequestId": "xx",
        "Logsets": [
            {
                "Tags": [
                    {
                        "Value": "xx",
                        "Key": "xx"
                    }
                ],
                "CreateTime": "xx",
                "RoleName": "xx",
                "TopicCount": 0,
                "LogsetName": "xx",
                "LogsetId": "xx"
            }
        ]
    }
}
```

