**Example 1: 查看告警列表**



Input: 

```
tccli csip DescribeCosAlarmList --cli-unfold-argument  \
    --Filter.Limit 10 \
    --Filter.Offset 0 \
    --Filter.Filters.0.Name BucketName \
    --Filter.Filters.0.Values brainzhao-test-251002343 \
    --Filter.Filters.0.OperatorType 9 \
    --Filter.StartTime 2026-03-10 00:00:00 \
    --Filter.EndTime 2026-03-14 00:00:00
```

Output: 
```
{
    "Response": {
        "Data": [
            {
                "AccountIdentify": 1,
                "AccountMainNickName": "",
                "AccountNickName": "测试环境账号",
                "AccountUin": "100000007008",
                "AlarmId": 8523,
                "AlarmTimestamp": 1773374151000,
                "AppId": 251002343,
                "BucketAccessWay": "specify",
                "BucketMarker": "",
                "BucketName": "test-251002111",
                "BucketRegion": "广东 广州",
                "BucketRegionCode": "ap-guangzhou",
                "BucketTagInfo": "null",
                "CategoryDetails": [
                    {
                        "CategoryId": 356,
                        "CategoryName": "个人信息",
                        "RuleSet": [
                            {
                                "LevelId": 10,
                                "LevelName": "一般",
                                "LevelScore": 1,
                                "RuleId": 6600,
                                "RuleName": "姓名"
                            }
                        ]
                    }
                ],
                "HandleStatus": 0,
                "PolicyAbnormalType": 1,
                "PolicyDescription": "匿名获取存储桶或对象策略，返回值为 200",
                "PolicyId": 2281,
                "PolicyName": "wx告警-202511062129",
                "PolicyRiskLevel": 3
            }
        ],
        "Total": 18,
        "RequestId": "b6a18fec-7234-49e5-b82c-e75461e29d18"
    }
}
```

