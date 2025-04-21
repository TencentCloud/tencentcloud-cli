**Example 1: DescribeSearchKb接口示例**



Input: 

```
tccli ioa DescribeSearchKb --cli-unfold-argument  \
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
    --List 字符串
```

Output: 
```
{
    "Response": {
        "Data": {
            "Item": [
                {
                    "PubDate": "abc",
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

**Example 2: DescribeSearchKb**

DescribeSearchKb

Input: 

```
tccli ioa DescribeSearchKb --cli-unfold-argument  \
    --Cond.PageSize 13 \
    --Cond.PageNum 1
```

Output: 
```
{
    "Response": {
        "Error": {
            "Code": "AuthFailure.SignatureFailure",
            "Message": "请求签名验证失败，请检查您的签名计算是否正确。"
        },
        "RequestId": "86b8a2af-db72-4869-a311-12271cb3e390"
    }
}
```

