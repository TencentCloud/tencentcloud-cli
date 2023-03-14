**Example 1: 查询指定时间内外部联系人详情**

通过时间段查询外部联系人详情

Input: 

```
tccli wav QueryExternalContactDetailByDate --cli-unfold-argument  \
    --Cursor 2Kgdu51quLaeNJSlwb79im883bftBE9d9Emju5I2MVw= \
    --Limit 100 \
    --BeginTime 1647187200 \
    --EndTime 1647273600
```

Output: 
```
{
    "Response": {
        "NextCursor": "2Kgdu51quLaeNJSlwb79im883bftBE9d9Emju5I2MVw=",
        "PageData": [
            {
                "Customer": {
                    "ExternalUserId": "wmQIM2CwAAE-JSOVGMzsRayI3ow5kGzQ",
                    "Gender": 1,
                    "Name": "文",
                    "Type": 1,
                    "UnionId": "ozynqsulJFCZ2z1aYeS8h-nuasdAAA",
                    "Phone": "134****3232"
                },
                "FollowUser": [
                    {
                        "UserId": "rocky",
                        "Remark": "备注",
                        "Description": "描述",
                        "CreateTime": 1618322621,
                        "AddWay": 0,
                        "OperUserId": "wmQIM2CwAAE-JSOVGMzsRayI3ow5kGzQ",
                        "Tags": [
                            {
                                "GroupName": "标签分组名称",
                                "TagName": "标签名称",
                                "Type": 1,
                                "TagId": "etAJ2GCAAAXtWyujaWJHDDGi0mACHAAA"
                            }
                        ],
                        "SalesName": "张三",
                        "DepartmentIdList": [
                            0
                        ]
                    }
                ]
            }
        ],
        "RequestId": "fea177dd-9fa6-4e76-9c8f-67f5a21f20bb"
    }
}
```

