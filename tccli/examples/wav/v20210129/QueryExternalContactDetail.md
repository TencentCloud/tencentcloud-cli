**Example 1: 查询外部联系人详情**



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
        "NextCursor": "",
        "RequestId": "482482d3-1631-4c41-a42a-41809d0e5593",
        "Customer": {
            "Type": 1,
            "Phone": "",
            "UnionId": "o1MJd6WzhNPBPLuXID6gpbHY2Mko",
            "ExternalUserId": "wmpqy2CAAALJVRD88JLOUVONlJS9c7nA",
            "Gender": 1,
            "Name": "艺术就是派大星"
        },
        "FollowUser": [
            {
                "OperUserId": "wmpqy2CAAALJVRD88JLOUVONlJS9c7nA",
                "Description": "",
                "AddWay": 3,
                "UserId": "TaXun",
                "CreateTime": 1621849569,
                "Tags": [
                    {
                        "GroupName": "个人标签",
                        "Type": 2,
                        "TagId": "etpqy2CAAA4au5I00lvVcnlZ_berhx1g",
                        "TagName": "标签名称"
                    }
                ],
                "Remark": "备注"
            }
        ]
    }
}
```

