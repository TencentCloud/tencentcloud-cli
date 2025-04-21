**Example 1: DescribeIgnoreKbs接口示例**



Input: 

```
tccli ioa DescribeIgnoreKbs --cli-unfold-argument  \
    --Cond.Sort.Field 字符串 \
    --Cond.Sort.Order 字符串 \
    --Cond.FilterGroups.0.Filters.0.Operator 字符串 \
    --Cond.FilterGroups.0.Filters.0.Field 字符串 \
    --Cond.FilterGroups.0.Filters.0.Values 字符串 \
    --Cond.PageNum 1 \
    --Cond.Filters.0.Operator 字符串 \
    --Cond.Filters.0.Field 字符串 \
    --Cond.Filters.0.Values 字符串 \
    --Cond.PageSize 10 \
    --Mid F1AFD85EC54480393C546B99C7CD014963761895
```

Output: 
```
{
    "Response": {
        "Data": {
            "Item": [
                {
                    "Ignore": 0,
                    "Kb": "abc",
                    "Id": 0,
                    "SecurityType": 0,
                    "Name": "abc"
                }
            ],
            "Page": {
                "PageSize": 1,
                "PageNum": 1,
                "PageCount": 1,
                "Total": 1
            }
        },
        "RequestId": "abc"
    }
}
```

**Example 2: DescribeIgnoreKbs**

DescribeIgnoreKbs

Input: 

```
tccli ioa DescribeIgnoreKbs --cli-unfold-argument  \
    --Cond.PageSize 1 \
    --Cond.PageNum 1 \
    --Mid 1234
```

Output: 
```
{
    "Response": {
        "Error": {
            "Code": "InternalError",
            "Message": "内部服务错误，请稍后重试。"
        },
        "RequestId": "a7e73482-81d0-4e13-b601-f13db7b5417a"
    }
}
```

