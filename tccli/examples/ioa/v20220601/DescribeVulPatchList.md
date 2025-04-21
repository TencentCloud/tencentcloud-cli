**Example 1: 查看漏洞补丁列表**



Input: 

```
tccli ioa DescribeVulPatchList --cli-unfold-argument  \
    --OsType 0
```

Output: 
```
{
    "Response": {
        "Data": {
            "Items": [
                {
                    "NameChinese": "abc",
                    "IgnoreDeviceCount": 0,
                    "DescribeChinese": "abc",
                    "DescribeEnglish": "abc",
                    "NameChineseTraditional": "abc",
                    "PublishDate": "abc",
                    "PatchKb": "abc",
                    "Id": 0,
                    "SysDescriptions": [
                        "abc"
                    ],
                    "UserId": 0,
                    "Utime": "abc",
                    "Kb": "abc",
                    "HasKbDeviceCount": 0,
                    "SysDescription": "abc",
                    "NoKbDeviceCount": 0,
                    "Itime": "abc",
                    "UnFixDeviceList": "abc",
                    "SecurityType": 0,
                    "GroupId": 0,
                    "NameEnglish": "abc",
                    "UnFixDeviceCount": 0,
                    "DescribeChineseTraditional": "abc",
                    "Systems": [
                        0
                    ]
                }
            ],
            "Paging": {
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

**Example 2: DescribeVulPatchList**

DescribeVulPatchList

Input: 

```
tccli ioa DescribeVulPatchList --cli-unfold-argument  \
    --OsType 0 \
    --Condition.PageSize 10 \
    --Condition.PageNum 0
```

Output: 
```
{
    "Response": {
        "Error": {
            "Code": "AuthFailure.SignatureFailure",
            "Message": "请求签名验证失败，请检查您的签名计算是否正确。"
        },
        "RequestId": "fc2e4909-4b88-488b-92b1-47e0bd9f7743"
    }
}
```

