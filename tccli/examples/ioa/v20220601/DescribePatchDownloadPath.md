**Example 1: DescribePatchDownloadPath接口示例**



Input: 

```
tccli ioa DescribePatchDownloadPath --cli-unfold-argument  \
    --Kb 字符串 \
    --Cond.Sort.Field 字符串 \
    --Cond.Sort.Order 字符串 \
    --Cond.FilterGroups.0.Filters.0.Operator 字符串 \
    --Cond.FilterGroups.0.Filters.0.Field 字符串 \
    --Cond.FilterGroups.0.Filters.0.Values 字符串 \
    --Cond.PageNum 1 \
    --Cond.Filters.0.Operator 字符串 \
    --Cond.Filters.0.Field 字符串 \
    --Cond.Filters.0.Values 字符串 \
    --Cond.PageSize 10
```

Output: 
```
{
    "Response": {
        "RequestId": "4a3d1c4f-9d01-40b3-84e9-95736e73949e",
        "Data": {
            "Page": {
                "PageSize": 10,
                "PageNum": 1,
                "PageCount": 0,
                "Total": 0
            }
        }
    }
}
```

