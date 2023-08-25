**Example 1: 新增分类分级模板**



Input: 

```
tccli dsgc CreateDSPAComplianceGroup --cli-unfold-argument  \
    --LevelGroupId 1 \
    --DspaId dspa-001 \
    --Name task \
    --Description 扫描任务
```

Output: 
```
{
    "Response": {
        "RequestId": "20569756-56ba-4a13-b545-e1528d5cb239",
        "ComplianceGroupId": 1
    }
}
```

