**Example 1: 查询活动列表**



Input: 

```
tccli wav QueryActivityList --cli-unfold-argument  \
    --Limit 1
```

Output: 
```
{
    "Response": {
        "NextCursor": "xxx",
        "RequestId": "c211f8cc-fb98-4a05-93bf-3e7ccb089592",
        "PageData": [
            {
                "ActivityState": 20,
                "ActivityName": "xxx",
                "EndTime": 111111111,
                "ActivityId": 111111111111111111,
                "UpdateTime": 111111111,
                "StartTime": 111111111,
                "ActivityType": 101,
                "PrivacyAgreementId": "xxx",
                "MainPhoto": "xxx",
                "ActivityDataList": "{\"couponTypeList\":[1],\"couponInfoList\":[{\"couponId\":\"111111111111\",\"couponName\":\"购车车款减免券001\",\"thresholdAmount\":10000000,\"discountAmount\":500000,\"discountPercentage\":0,\"couponType\":1,\"availableTimeType\":1,\"availableBeginTime\":0,\"availableEndTime\":1111111111}]}"
            }
        ]
    }
}
```

