**Example 1: DescribeSearchAccountGroupTree**



Input: 

```
tccli ioa DescribeSearchAccountGroupTree --cli-unfold-argument  \
    --Condition.PageNum 1 \
    --Condition.Filters.0.Operator like \
    --Condition.Filters.0.Field Name \
    --Condition.Filters.0.Values 开发 \
    --Condition.PageSize 10 \
    --AccountGroupId 28
```

Output: 
```
{
    "Response": {
        "Data": {
            "Items": [
                {
                    "ParentOrgId": "0",
                    "Utime": "2022-06-26 18:35:58",
                    "Id": 28,
                    "Itime": "2022-06-26 18:35:58",
                    "ExtraInfo": "",
                    "Name": "企业微信2",
                    "ParentId": 22,
                    "Description": "描述信息",
                    "Source": 0,
                    "NamePath": "全网账户.企业微信2",
                    "IdPath": "22.28",
                    "ReadOnly": false,
                    "IdPathArr": [
                        22,
                        28
                    ],
                    "OrgId": "28"
                },
                {
                    "ParentOrgId": "28",
                    "Utime": "2022-06-28 09:57:00",
                    "Id": 37,
                    "Itime": "2022-06-28 09:57:00",
                    "ExtraInfo": "{}",
                    "Name": "广州扬基信息科技有限公司",
                    "ParentId": 28,
                    "Description": "",
                    "Source": 10902,
                    "NamePath": "全网账户.企业微信2.广州扬基信息科技有限公司",
                    "IdPath": "22.28.37",
                    "ReadOnly": false,
                    "IdPathArr": [
                        22,
                        28,
                        37
                    ],
                    "OrgId": "9100ddb2-4f00-32db-a3a2-6b0bf0511195"
                },
                {
                    "ParentOrgId": "9100ddb2-4f00-32db-a3a2-6b0bf0511195",
                    "Utime": "2022-06-28 09:57:00",
                    "Id": 39,
                    "Itime": "2022-06-28 09:57:00",
                    "ExtraInfo": "{}",
                    "Name": "开发测试",
                    "ParentId": 37,
                    "Description": "",
                    "Source": 10902,
                    "NamePath": "全网账户.企业微信2.广州扬基信息科技有限公司.开发测试",
                    "IdPath": "22.28.37.39",
                    "ReadOnly": false,
                    "IdPathArr": [
                        22,
                        28,
                        37,
                        39
                    ],
                    "OrgId": "9efa3d18-8d67-3c19-b487-dbce8258ab25"
                },
                {
                    "ParentOrgId": "9efa3d18-8d67-3c19-b487-dbce8258ab25",
                    "Utime": "2022-06-28 09:57:00",
                    "Id": 48,
                    "Itime": "2022-06-28 09:57:00",
                    "ExtraInfo": "{}",
                    "Name": "开发",
                    "ParentId": 39,
                    "Description": "",
                    "Source": 10902,
                    "NamePath": "全网账户.企业微信2.广州扬基信息科技有限公司.开发测试.开发",
                    "IdPath": "22.28.37.39.48",
                    "ReadOnly": false,
                    "IdPathArr": [
                        22,
                        28,
                        37,
                        39,
                        48
                    ],
                    "OrgId": "6341df7c-0bf6-3d43-b853-7ad88bb20180"
                }
            ]
        },
        "RequestId": "103b7e8a-90a6-4511-a2ac-026401fedf78"
    }
}
```

