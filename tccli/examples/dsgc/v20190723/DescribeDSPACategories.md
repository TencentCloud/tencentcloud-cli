**Example 1: 获取分类列表**



Input: 

```
tccli dsgc DescribeDSPACategories --cli-unfold-argument  \
    --DspaId dspa-001 \
    --Limit 1 \
    --Name 财务信息 \
    --Offset 0
```

Output: 
```
{
    "Response": {
        "RequestId": "20569756-56ba-4a13-b545-e1528d5cb239",
        "TotalCount": 1,
        "Items": [
            {
                "Source": 1,
                "CategoryId": 1,
                "Name": "财务信息"
            }
        ]
    }
}
```

