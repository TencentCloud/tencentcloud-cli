**Example 1: 获取分类分级模板列表**



Input: 

```
tccli dsgc DescribeDSPAComplianceGroups --cli-unfold-argument  \
    --DspaId dspa-001 \
    --Name task
```

Output: 
```
{
    "Response": {
        "Items": [
            {
                "ComplianceGroupId": 1,
                "Name": "通用规则集",
                "Description": "通用规则集的描述",
                "ComplianceGroupType": 0,
                "ComplianceGroupRules": [
                    {
                        "RuleId": 0,
                        "RuleName": "手机",
                        "CategoryId": 0,
                        "LevelId": 0,
                        "CategoryName": "个人信息",
                        "LevelRiskName": "敏感"
                    }
                ],
                "LevelGroupId": 1,
                "Disabled": true,
                "IsAlias": true
            }
        ],
        "TotalCount": 0,
        "RequestId": "91c7a73v-e540-4780-8b8e-74e0b65b4f1a"
    }
}
```

**Example 2: 主模板字段返回示例**

扩展主模板标志字段

Input: 

```
tccli dsgc DescribeDSPAComplianceGroups --cli-unfold-argument  \
    --DspaId dspa-e7899f91
```

Output: 
```
{
    "Response": {
        "Items": [
            {
                "ComplianceGroupId": 6,
                "ComplianceGroupRules": [],
                "ComplianceGroupType": 1,
                "Description": "参考 GB/T 42013-2022《信息安全技术快递物流服务数据安全要求》",
                "Disabled": true,
                "IsAlias": false,
                "LevelGroupId": 2,
                "Name": "快递物流行业分类分级模板"
            },
            {
                "ComplianceGroupId": 5,
                "ComplianceGroupRules": [],
                "ComplianceGroupType": 1,
                "Description": "参考 YD/T 3751-2020《车联网信息服务数据安全技术要求》",
                "Disabled": true,
                "IsAlias": false,
                "LevelGroupId": 3,
                "Name": "车联网行业分类分级模板"
            },
            {
                "ComplianceGroupId": 4,
                "ComplianceGroupRules": [],
                "ComplianceGroupType": 1,
                "Description": "参考 JR∕T 0197-2020《金融数据安全数据安全分级指南》",
                "Disabled": true,
                "IsAlias": false,
                "LevelGroupId": 2,
                "Name": "金融数据安全分类分级模板"
            },
            {
                "ComplianceGroupId": 3,
                "ComplianceGroupRules": [],
                "ComplianceGroupType": 1,
                "Description": "参考 GB/T 35273-2020《信息安全技术个人信息安全规范》",
                "Disabled": false,
                "IsAlias": false,
                "LevelGroupId": 1,
                "Name": "个人身份信息识别模板"
            },
            {
                "ComplianceGroupId": 2,
                "ComplianceGroupRules": [],
                "ComplianceGroupType": 1,
                "Description": "参考 JR∕T 0171-2020《个人金融信息保护技术规范》",
                "Disabled": true,
                "IsAlias": false,
                "LevelGroupId": 1,
                "Name": "个人金融信息保护技术规范"
            },
            {
                "ComplianceGroupId": 1,
                "ComplianceGroupRules": [],
                "ComplianceGroupType": 0,
                "Description": "通用规则集",
                "Disabled": false,
                "IsAlias": false,
                "LevelGroupId": 1,
                "Name": "通用规则集"
            }
        ],
        "RequestId": "232796e7-693f-43ca-a14c-134ad4a8b702",
        "TotalCount": 6
    }
}
```

