**Example 1: DescribeVulDeviceList**



Input: 

```
tccli ioa DescribeVulDeviceList --cli-unfold-argument  \
    --VulRange 字符串 \
    --Cond.Sort.Field 字符串 \
    --Cond.Sort.Order 字符串 \
    --Cond.FilterGroups.0.Filters.0.Operator 字符串 \
    --Cond.FilterGroups.0.Filters.0.Field 字符串 \
    --Cond.FilterGroups.0.Filters.0.Values 字符串 \
    --Cond.PageNum 1 \
    --Cond.Filters.0.Operator 字符串 \
    --Cond.Filters.0.Field 字符串 \
    --Cond.Filters.0.Values 字符串 \
    --Cond.PageSize 1 \
    --GroupId 1 \
    --SecurityType 1
```

Output: 
```
{
    "Response": {
        "RequestId": "1ace6ab5-8b3b-46cf-8a1a-954a1f0d1c9b",
        "Data": {
            "Item": [
                {
                    "FixedDeviceCount": 0,
                    "Kb": "KB2028551",
                    "NameChinese": "Windows 7 更新程序",
                    "NameEnglish": "Update for Windows 7",
                    "GroupId": 1,
                    "DescChinese": "本更新程序可解决打印的 XPS 包含视觉画笔并转换为基于 GDI 的打印机时，某些元素被剪辑的情况。您还应安装此更新程序以支持即将发行的 Internet Explorer 9 平台预览版本中的功能。",
                    "SysDescription": [
                        "Windows 7 X64;"
                    ],
                    "DescEnglish": "This update resolves instances where certain elements are clipped when printing an XPS containing visual brushes with transforms to a GDI-based printer.",
                    "Id": 5015,
                    "PubDate": "2010-10-27",
                    "SecurityType": 1,
                    "UnfixDeviceCount": 0,
                    "IgnoreDeviceCount": 0
                }
            ],
            "Page": {
                "PageSize": 1,
                "PageNum": 1,
                "PageCount": 1420,
                "Total": 1420
            }
        }
    }
}
```

**Example 2: DescribeVulDeviceList--主要发测试**

DescribeVulDeviceList

Input: 

```
tccli ioa DescribeVulDeviceList --cli-unfold-argument  \
    --VulRange 1 \
    --Cond.PageSize 1 \
    --Cond.PageNum 1 \
    --GroupId 1 \
    --SecurityType 1
```

Output: 
```
{
    "Response": {
        "Error": {
            "Code": "AuthFailure.SignatureFailure",
            "Message": "请求签名验证失败，请检查您的签名计算是否正确。"
        },
        "RequestId": "519c353e-4d2f-4f18-a6bf-0e0adb874a7e"
    }
}
```

