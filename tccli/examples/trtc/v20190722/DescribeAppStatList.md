**Example 1: 获取用户名下的应用列表**

获取用户名下的应用列表

Input: 

```
tccli trtc DescribeAppStatList --cli-unfold-argument  \
    --OrderField create_time \
    --OrderType 0 \
    --Offset 0 \
    --Limit 3 \
    --GmeFlag 0
```

Output: 
```
{
    "Response": {
        "SdkAppInfos": [
            {
                "Status": 1,
                "LastDayCC": 1,
                "Description": "string",
                "HasAccount": 1,
                "InWhiteList": false,
                "CurMonthCC": 1,
                "BizScheme": 1,
                "PrewhiteFlag": 1,
                "AccountMode": 1,
                "Name": "string",
                "RegisterFrom": 1,
                "LastDay": 1,
                "BizSubScheme": 1,
                "UiMode": 0,
                "CreateTime": "string",
                "License": "string",
                "SubProductCode": "string",
                "ID": 1,
                "TagList": [
                    {
                        "TagKey": "string",
                        "TagValue": "string"
                    }
                ],
                "UsageMode": [
                    0,
                    1,
                    2
                ]
            }
        ],
        "RequestId": "string",
        "TotalNum": 1
    }
}
```

