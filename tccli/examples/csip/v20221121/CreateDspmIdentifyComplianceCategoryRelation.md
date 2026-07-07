**Example 1: 创建dspm数据识别模板分类关联**



Input: 

```
tccli csip CreateDspmIdentifyComplianceCategoryRelation --cli-unfold-argument  \
    --ComplianceId 10001 \
    --CategoryId 358 \
    --ParentCategoryId -1 \
    --MemberId mem-12e1dsda
```

Output: 
```
{
    "Response": {
        "RequestId": "86f82abd-6a37-4141-8179-b4040fb04d28"
    }
}
```

