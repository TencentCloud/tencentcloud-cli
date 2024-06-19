**Example 1: 获取分级列表**



Input: 

```
tccli dsgc DescribeDSPALevelGroups --cli-unfold-argument  \
    --DspaId dspa-00000000 \
    --Name test
```

Output: 
```
{
    "Response": {
        "RequestId": "b7f2cb00-e759-436e-97dc-6c95c9b61005",
        "TotalCount": 1,
        "Items": [
            {
                "LevelGroupId": 11985,
                "RefComplianceCnt": 6,
                "LevelGroupName": "系统-敏感程度",
                "Source": 1,
                "LevelGroupDesc": "",
                "LevelDetail": [
                    {
                        "LevelGroupId": 11985,
                        "LevelRiskName": "1",
                        "LevelRiskScore": 1,
                        "LevelId": 12010
                    },
                    {
                        "LevelGroupId": 11985,
                        "LevelRiskName": "2",
                        "LevelRiskScore": 2,
                        "LevelId": 12011
                    }
                ],
                "RefCompliance": [
                    {
                        "Name": "测试扫描任务抓包1",
                        "LevelGroupId": 11985,
                        "ComplianceGroupRules": [
                            {
                                "RuleName": "测试规则1",
                                "CategoryId": 10794,
                                "LevelId": 12011,
                                "RuleId": 228
                            }
                        ],
                        "ComplianceGroupType": 2,
                        "Description": "",
                        "ComplianceGroupId": 14795
                    },
                    {
                        "Name": "测试扫描任务抓包2",
                        "LevelGroupId": 11985,
                        "ComplianceGroupRules": [],
                        "ComplianceGroupType": 2,
                        "Description": "",
                        "ComplianceGroupId": 14796
                    }
                ]
            }
        ]
    }
}
```

