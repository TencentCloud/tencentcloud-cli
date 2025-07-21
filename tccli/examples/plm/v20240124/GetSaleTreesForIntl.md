**Example 1: test**



Input: 

```
tccli plm GetSaleTreesForIntl --cli-unfold-argument  \
    --PortalStaffId abc22 \
    --PortalStaffUa abc33 \
    --PortalStaffIp abc44 \
    --PortalStaffName abc55 \
    --StatusList 0 \
    --Status 9999
```

Output: 
```
{
    "Response": {
        "List": [
            {
                "CenterList": [],
                "Child": [
                    {
                        "CenterList": [],
                        "Child": [],
                        "Code": "XB001035",
                        "DepartmentList": [],
                        "EnAbbreviation": "xuojinsss",
                        "Modifier": "",
                        "Name": "测试新增0913",
                        "NameEn": "",
                        "Status": 2,
                        "UpdateTime": "",
                        "Weight": 0
                    }
                ],
                "Code": "XA001034",
                "DepartmentList": [],
                "EnAbbreviation": "shuoxie1",
                "Modifier": "",
                "Name": "测试新增0913",
                "NameEn": "English name of sales catalog 8",
                "Status": 2,
                "UpdateTime": "",
                "Weight": 11
            },
            {
                "CenterList": [],
                "Child": [
                    {
                        "CenterList": [],
                        "Child": [],
                        "Code": "XB001014",
                        "DepartmentList": [],
                        "EnAbbreviation": "sdsdsdsds",
                        "Modifier": "",
                        "Name": "zanderfang测试销售目录L2的名称5",
                        "NameEn": "",
                        "Status": 1,
                        "UpdateTime": "",
                        "Weight": 0
                    },
                    {
                        "CenterList": [],
                        "Child": [],
                        "Code": "XB001104",
                        "DepartmentList": [],
                        "EnAbbreviation": "shuoxie3",
                        "Modifier": "",
                        "Name": "ceshixa1",
                        "NameEn": "ceshixa1",
                        "Status": 1,
                        "UpdateTime": "",
                        "Weight": 0
                    }
                ],
                "Code": "XA001004",
                "DepartmentList": [],
                "EnAbbreviation": "jialeyingwensuoxie",
                "Modifier": "",
                "Name": "zanderfang测试销售目录L1的名称5",
                "NameEn": "English name of sales catalog 6",
                "Status": 1,
                "UpdateTime": "",
                "Weight": 10
            }
        ],
        "RequestId": "8c9d8542-0977-4c5a-b9e0-15b4cf86607b"
    }
}
```

