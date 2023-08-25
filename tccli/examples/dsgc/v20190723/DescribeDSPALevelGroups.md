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
        "Items": [
            {
                "LevelGroupDesc": "xx",
                "RefComplianceCnt": 1,
                "LevelDetail": [
                    {
                        "LevelGroupId": 1,
                        "LevelRiskScore": 1,
                        "LevelId": 1,
                        "LevelRiskName": "xx"
                    }
                ],
                "LevelGroupName": "xx",
                "Source": 1,
                "LevelGroupId": 1,
                "RefCompliance": [
                    {
                        "Name": "xx",
                        "LevelGroupId": 1,
                        "ComplianceGroupRules": [
                            {
                                "RuleId": 0,
                                "RuleName": "xx",
                                "LevelId": 0,
                                "CategoryId": 0
                            }
                        ],
                        "ComplianceGroupId": 3,
                        "ComplianceGroupType": 1,
                        "Description": "xx"
                    }
                ]
            }
        ],
        "RequestId": "xx",
        "TotalCount": 1
    }
}
```

