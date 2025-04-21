**Example 1: DescribeInstallDeviceList接口示例**



Input: 

```
tccli ioa DescribeInstallDeviceList --cli-unfold-argument  \
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
    --Cond.PageSize 10 \
    --GroupId 1
```

Output: 
```
{
    "Response": {
        "Data": {
            "Item": [
                {
                    "MacAddr": "abc",
                    "Name": "abc",
                    "GroupNamePath": "abc",
                    "Ip": "abc",
                    "Mid": "abc",
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

**Example 2: DescribeInstallDeviceList**

DescribeInstallDeviceList

Input: 

```
tccli ioa DescribeInstallDeviceList --cli-unfold-argument  \
    --Kb 123342 \
    --Cond.PageSize 12 \
    --Cond.PageNum 1 \
    --GroupId 1
```

Output: 
```
{
    "Response": {
        "Error": {
            "Code": "AuthFailure.SignatureFailure",
            "Message": "请求签名验证失败，请检查您的签名计算是否正确。"
        },
        "RequestId": "aaab2361-f093-4d60-be82-5523dc43275e"
    }
}
```

