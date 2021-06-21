**Example 1: 获取客户详情**



Input: 

```
tccli wav QueryExternalContactDetail --cli-unfold-argument  \
    --ExternalUserId 2Kgdu51quLaeNJSlwb79im883bftBE9d9Emju5I2MVw \
    --Cursor xxxx \
    --Limit 10
```

Output: 
```
{
    "Response": {
        "Customer": {
            "Gender": 1,
            "Type": 1,
            "Phone": "13xxxxxxxxx",
            "Name": "xx"
        },
        "NextCursor": "xx",
        "FollowUser": [
            {
                "Remark": "xx",
                "Description": "xx",
                "Tags": [
                    {
                        "GroupName": "xx",
                        "TagId": "xx",
                        "Type": 1,
                        "TagName": "xx"
                    }
                ],
                "OperUserId": "xx",
                "UserId": "xx",
                "AddWay": 0
            }
        ],
        "RequestId": "xx"
    }
}
```

