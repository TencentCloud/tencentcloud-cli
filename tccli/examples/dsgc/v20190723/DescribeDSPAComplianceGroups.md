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
        "RequestId": "d722c0ba-ad06-4e10-9941-e1eeb044fbf8",
        "TotalCount": 1,
        "Items": [
            {
                "ComplianceGroupId": 3,
                "Name": "aaaq",
                "Description": "ddd",
                "ComplianceGroupType": 1
            }
        ]
    }
}
```

