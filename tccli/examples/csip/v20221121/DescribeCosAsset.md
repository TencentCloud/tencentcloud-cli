**Example 1: 查看COS资产列表**



Input: 

```
tccli csip DescribeCosAsset --cli-unfold-argument  \
    --Filter.Limit 10 \
    --Filter.Filters.0.Name BucketName \
    --Filter.Filters.0.Values brainzhao-test-1302396215 \
    --Filter.Filters.0.OperatorType 9
```

Output: 
```
{
    "Response": {
        "Data": [
            {
                "AppId": 1302396215,
                "BucketAccessWay": {
                    "AccessAkCount": 0,
                    "AccessRoleCount": 31,
                    "AccessType": "specify",
                    "AccessUserCount": 43
                },
                "BucketAlarmList": [],
                "BucketId": 0,
                "BucketInvokeSourceIpCount": 0,
                "BucketMarker": "",
                "BucketName": "brainzhao-test-1302396215",
                "BucketOwnerNickName": "声声乌龙",
                "BucketOwnerUin": "100014592178",
                "BucketRegion": "广东 广州",
                "BucketRegionCode": "ap-guangzhou",
                "BucketRiskList": [
                    {
                        "PolicyCount": 3,
                        "PolicyType": 2,
                        "PolicyTypeName": "权限过大"
                    }
                ],
                "BucketSecuritySuggestion": 2,
                "BucketTagInfo": "[{\"Key\":\"tke-lb-serviceuuid\",\"Value\":\"935e9f8f-0ed3-4b3a-b374-087538cc57eb\"}]",
                "CreateTime": 1754639424000,
                "DataScanInfo": {
                    "CategoryDetails": [
                        {
                            "CategoryId": 356,
                            "CategoryName": "个人信息",
                            "RuleSet": [
                                {
                                    "LevelId": 10,
                                    "LevelName": "一般",
                                    "LevelScore": 1,
                                    "RuleId": 5802,
                                    "RuleName": "生日"
                                }
                            ]
                        }
                    ],
                    "ErrorInfo": "",
                    "LatestScanTime": "2026-02-26 12:00:00",
                    "Status": 2
                },
                "LastAccessTime": 0,
                "MonitorStatus": 1
            }
        ],
        "Total": 1,
        "RequestId": "b701d18d-f68f-44f7-a46a-8b62efa20bea"
    }
}
```

