**Example 1: 查询账号列表**



Input: 

```
tccli ioa DescribeAccountGroups --cli-unfold-argument ```

Output: 
```
{
    "Response": {
        "Data": {
            "Items": [
                {
                    "Source": 0,
                    "IdPath": "1.30",
                    "ImportType": "zijian",
                    "Id": 30,
                    "UserTotal": 0,
                    "IsLeaf": false,
                    "ReadOnly": false,
                    "ParentId": 1,
                    "ExtraInfo": "",
                    "OrgId": "30",
                    "NamePath": "分组路径",
                    "Description": "",
                    "IdPathArr": [
                        1,
                        30
                    ],
                    "Utime": "2022-07-21 10:24:11",
                    "Name": "用户名",
                    "Itime": "2022-07-21 10:24:11",
                    "ParentOrgId": "0",
                    "MiniIamId": ""
                }
            ],
            "Page": {
                "PageSize": 10,
                "PageNum": 0,
                "Total": 4,
                "PageCount": 1
            }
        },
        "RequestId": "1658388211.551832"
    }
}
```

