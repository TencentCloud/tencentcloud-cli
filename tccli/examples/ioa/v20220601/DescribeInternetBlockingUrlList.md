**Example 1: 获取上网拦截列表**

获取上网拦截列表

Input: 

```
tccli ioa DescribeInternetBlockingUrlList --cli-unfold-argument  \
    --Condition.Filters.0.Field abc \
    --Condition.Filters.0.Operator abc \
    --Condition.Filters.0.Values abc \
    --Condition.FilterGroups.0.Filters.0.Field abc \
    --Condition.FilterGroups.0.Filters.0.Operator abc \
    --Condition.FilterGroups.0.Filters.0.Values abc \
    --Condition.Sort.Field abc \
    --Condition.Sort.Order abc \
    --Condition.PageSize 0 \
    --Condition.PageNum 0
```

Output: 
```
{
    "Response": {
        "Data": {
            "Page": {
                "PageSize": 1,
                "PageNum": 1,
                "PageCount": 1,
                "Total": 1
            },
            "Items": [
                {
                    "Id": 0,
                    "CategoryId": "abc",
                    "Host": "abc",
                    "HostName": "abc"
                }
            ]
        },
        "RequestId": "abc"
    }
}
```

