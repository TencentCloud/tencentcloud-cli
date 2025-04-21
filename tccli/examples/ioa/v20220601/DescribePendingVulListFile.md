**Example 1: DescribePendingVulListFile接口示例**



Input: 

```
tccli ioa DescribePendingVulListFile --cli-unfold-argument  \
    --OnlineStatus 5 \
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
    --GroupId 1 \
    --DeviceRange 字符串
```

Output: 
```
{
    "Response": {
        "RequestId": "794dbb00-038c-4a2f-af02-6a5211f8531f",
        "Data": {
            "DownloadURL": "https://ioa-dev-1-1258344699.cos.accelerate.myqcloud.com/on-premise/web-open-api/device_security/rmNEftgUIJ-%E6%BC%8F%E6%B4%9E%E4%BF%AE%E5%A4%8D-%E6%8C%89%E7%BB%88%E7%AB%AF%E6%9F%A5%E7%9C%8B-20221223111115.csv?q-sign-algorithm=sha1&q-ak=AKIDf9PPAfv0qQs8BzXsxnNincCWbQzJNDo9&q-sign-time=1671765305%3B1671768905&q-key-time=1671765305%3B1671768905&q-header-list=host&q-url-param-list=&q-signature=210036a82f60c23b1049c62ce8acd49a2ad9c324"
        }
    }
}
```

**Example 2: DescribePendingVulListFile**

DescribePendingVulListFile

Input: 

```
tccli ioa DescribePendingVulListFile --cli-unfold-argument  \
    --OnlineStatus 1 \
    --GroupId 1 \
    --DeviceRange 1
```

Output: 
```
{
    "Response": {
        "Error": {
            "Code": "AuthFailure.SignatureFailure",
            "Message": "请求签名验证失败，请检查您的签名计算是否正确。"
        },
        "RequestId": "2665aa23-8393-40fd-952b-35464bad6101"
    }
}
```

