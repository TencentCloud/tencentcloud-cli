**Example 1: 查询外部联系人详情**

通过外部联系人ID获取相应的详情信息

Input: 

```
tccli wav QueryExternalContactDetail --cli-unfold-argument  \
    --ExternalUserId 2Kgdu51quLaeNJSlwb79im883bftBE9d9Emju5I2MVw \
    --Cursor sHmJbhJZhCwwMYmSot50dl2Hs9qQvbP+pCUVxlm/oLU \
    --Limit 10
```

Output: 
```
{
    "Response": {
        "NextCursor": "abc",
        "Customer": {
            "ExternalUserId": "abc",
            "Gender": 0,
            "Name": "abc",
            "Type": 1,
            "UnionId": "abc",
            "Phone": "abc"
        },
        "FollowUser": [
            {
                "UserId": "abc",
                "Remark": "abc",
                "Description": "abc",
                "CreateTime": 1,
                "AddWay": 0,
                "OperUserId": "abc",
                "Tags": [
                    {
                        "GroupName": "abc",
                        "TagName": "abc",
                        "Type": 1,
                        "TagId": "abc"
                    }
                ]
            }
        ],
        "RequestId": "abc"
    }
}
```

