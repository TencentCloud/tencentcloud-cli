**Example 1: 获取分级列表**



Input: 

```
tccli dsgc DescribeDSPALevelGroups --cli-unfold-argument  \
    --DspaId dspa-8u9cas2a \
    --Name 内置分级组
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
                "LevelGroupName": "内置分级组",
                "Source": 1,
                "LevelGroupDesc": "系统内置敏感等级",
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
                        "Name": "扫描任务抓包1",
                        "LevelGroupId": 11985,
                        "ComplianceGroupRules": [
                            {
                                "RuleName": "规则1",
                                "CategoryId": 10794,
                                "LevelId": 12011,
                                "RuleId": 228
                            }
                        ],
                        "ComplianceGroupType": 2,
                        "Description": "关联的合规组",
                        "ComplianceGroupId": 14795
                    },
                    {
                        "Name": "扫描任务抓包2",
                        "LevelGroupId": 11985,
                        "ComplianceGroupRules": [
                            {
                                "RuleName": "规则2",
                                "CategoryId": 10762,
                                "LevelId": 12054,
                                "RuleId": 243
                            }
                        ],
                        "ComplianceGroupType": 2,
                        "Description": "关联的合规组2",
                        "ComplianceGroupId": 14796
                    }
                ]
            }
        ]
    }
}
```

