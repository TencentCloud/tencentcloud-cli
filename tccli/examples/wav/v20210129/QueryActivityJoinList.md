**Example 1: 查询活动列表**



Input: 

```
tccli wav QueryActivityJoinList --cli-unfold-argument  \
    --Limit 1 \
    --ActivityId 111111111111111111
```

Output: 
```
{
    "Response": {
        "NextCursor": "xxx",
        "RequestId": "332120d7-951e-4c43-9223-0c8b980a38d2",
        "PageData": [
            {
                "ActivityData": "{\"couponTypeList\":[1],\"couponInfoList\":[{\"couponId\":\"1111111111111111\",\"couponName\":\"购车车款减免券001\",\"thresholdAmount\":10000000,\"discountAmount\":500000,\"discountPercentage\":0,\"couponType\":1,\"availableTimeType\":1,\"availableBeginTime\":0,\"availableEndTime\":1111111111}]}",
                "SalesName": "xxx",
                "UserName": "参与者",
                "ActivityName": "满减",
                "SalesPhone": "xxx",
                "ActivityId": 111111111111111111,
                "CreateTime": 111111111,
                "LiveCodeId": 0,
                "JoinId": 111111111111111111,
                "JoinState": 1,
                "DuplicateLeadId": 111111111111111111,
                "UserPhone": "xxx",
                "UpdateTime": 111111111,
                "Duplicate": 2,
                "JoinTime": 111111111,
                "LeadId": 111111111111111111
            }
        ]
    }
}
```

