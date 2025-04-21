**Example 1: DescribeInstallKBList接口示例**



Input: 

```
tccli ioa DescribeInstallKBList --cli-unfold-argument  \
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
                    "Kb": "abc",
                    "InstallDate": "abc",
                    "PubDate": "abc",
                    "Title": "abc",
                    "SecurityType": 0,
                    "Desc": "abc"
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

**Example 2: DescribeInstallKBList**

DescribeInstallKBList

Input: 

```
tccli ioa DescribeInstallKBList --cli-unfold-argument  \
    --Cond.PageSize 1 \
    --Cond.PageNum 1 \
    --Mid 1234
```

Output: 
```
{
    "Response": {
        "Error": {
            "Code": "AuthFailure.SignatureFailure",
            "Message": "请求签名验证失败，请检查您的签名计算是否正确。"
        },
        "RequestId": "9998407c-a7b1-4571-a663-3d0685ce9512"
    }
}
```

