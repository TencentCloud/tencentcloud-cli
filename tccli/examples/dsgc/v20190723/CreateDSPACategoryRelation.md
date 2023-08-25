**Example 1: 创建分类关联关系**

创建分类关联关系

Input: 

```
tccli dsgc CreateDSPACategoryRelation --cli-unfold-argument  \
    --DspaId dspa-001 \
    --CategoryId 172 \
    --ParentCategoryId 167 \
    --ComplianceId 5
```

Output: 
```
{
    "Response": {
        "RequestId": "20569756-56ba-4a13-b545-e1528d5cb239"
    }
}
```

