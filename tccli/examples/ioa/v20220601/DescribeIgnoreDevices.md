**Example 1: DescribeIgnoreDevices接口示例**



Input: 

```
tccli ioa DescribeIgnoreDevices --cli-unfold-argument  \
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
        "Data": {
            "Item": [
                {
                    "Name": "abc",
                    "GroupNamePath": "abc",
                    "Ip": "abc",
                    "Mid": "abc",
                    "Ignore": 0,
                    "GroupName": "abc",
                    "Id": 0
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

**Example 2: DescribeIgnoreDevices**

DescribeIgnoreDevices

Input: 

```
tccli ioa DescribeIgnoreDevices --cli-unfold-argument  \
    --Kb KB!@#$ \
    --Cond.PageSize 10 \
    --Cond.PageNum 0
```

Output: 
```
{
    "Response": {
        "Error": {
            "Code": "AuthFailure.SignatureFailure",
            "Message": "请求签名验证失败，请检查您的签名计算是否正确。"
        },
        "RequestId": "6f443b78-64e8-49a3-8569-d2000f97af23"
    }
}
```

