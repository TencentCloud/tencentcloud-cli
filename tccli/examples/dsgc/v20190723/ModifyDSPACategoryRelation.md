**Example 1: 修改分类分级关系**

修改分类分级关系

Input: 

```
tccli dsgc ModifyDSPACategoryRelation --cli-unfold-argument  \
    --DspaId dspa-001 \
    --ComplianceId 1 \
    --CategoryId 169 \
    --MergedCategoryId 166
```

Output: 
```
{
    "Response": {
        "RequestId": "20569756-56ba-4a13-b545-e1528d5cb239"
    }
}
```

