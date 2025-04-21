**Example 1: 查询账号分组列表**



Input: 

```
tccli ioa DescribeAccountGroups --cli-unfold-argument  \
    --Deepin 1 \
    --Condition.Filters.0.Field Name \
    --Condition.Filters.0.Operator like \
    --Condition.Filters.0.Values 研发 \
    --ParentId 82119
```

Output: 
```
{
    "Response": {
        "Data": {
            "Items": [
                {
                    "Description": "这是一个研发部门",
                    "ExtraInfo": "{\"salt\": \"5b52ea107e85a7b46d2c1b15a5faf722\"}",
                    "Id": 510945,
                    "IdPath": "14632.82119.510943.510945",
                    "IdPathArr": [
                        14632,
                        82119,
                        510943,
                        510945
                    ],
                    "ImportType": "zijian",
                    "IsLeaf": false,
                    "Itime": "2024-10-21 14:34:01",
                    "LatestSyncResult": "Success",
                    "LatestSyncTime": "2024-10-20 09:00:01",
                    "MiniIamId": "13178683927JH5h7jtvXdCqPLKnC46gC",
                    "Name": "研发部",
                    "NamePath": "全网账户.pf自建.集团.研发部",
                    "OrgId": "510945",
                    "ParentId": 510943,
                    "ParentOrgId": "510943",
                    "ReadOnly": false,
                    "Source": 0,
                    "UserTotal": 1,
                    "Utime": "2024-10-21 14:34:16"
                },
                {
                    "Description": "这是一个研发组",
                    "ExtraInfo": "{\"salt\": \"5b52ea107e85a7b46d2c1b15a5faf722\"}",
                    "Id": 510947,
                    "IdPath": "14632.82119.510943.510945.510947",
                    "IdPathArr": [
                        14632,
                        82119,
                        510943,
                        510945,
                        510947
                    ],
                    "ImportType": "zijian",
                    "IsLeaf": true,
                    "Itime": "2024-10-21 14:34:37",
                    "LatestSyncResult": "Success",
                    "LatestSyncTime": "2024-10-20 09:00:01",
                    "MiniIamId": "13178683927JH5h7jtvXdCqPLKnC46gC",
                    "Name": "研发一组",
                    "NamePath": "全网账户.pf自建.集团.研发部.研发一组",
                    "OrgId": "510947",
                    "ParentId": 510945,
                    "ParentOrgId": "510945",
                    "ReadOnly": false,
                    "Source": 0,
                    "UserTotal": 0,
                    "Utime": "2024-10-21 14:34:37"
                },
                {
                    "Description": "这是另一个研发组",
                    "ExtraInfo": "{\"salt\": \"5b52ea107e85a7b46d2c1b15a5faf722\"}",
                    "Id": 510948,
                    "IdPath": "14632.82119.510943.510945.510948",
                    "IdPathArr": [
                        14632,
                        82119,
                        510943,
                        510945,
                        510948
                    ],
                    "ImportType": "zijian",
                    "IsLeaf": true,
                    "Itime": "2024-10-21 14:34:52",
                    "LatestSyncResult": "Success",
                    "LatestSyncTime": "2024-10-20 09:00:01",
                    "MiniIamId": "13178683927JH5h7jtvXdCqPLKnC46gC",
                    "Name": "研发二组",
                    "NamePath": "全网账户.pf自建.集团.研发部.研发二组",
                    "OrgId": "510948",
                    "ParentId": 510945,
                    "ParentOrgId": "510945",
                    "ReadOnly": false,
                    "Source": 0,
                    "UserTotal": 1,
                    "Utime": "2024-10-21 14:34:52"
                }
            ],
            "Page": {
                "PageCount": 1,
                "PageNum": 0,
                "PageSize": 10,
                "Total": 3
            }
        },
        "RequestId": "365d01ca-41d2-45b8-97d5-b8e5ce2c5148"
    }
}
```

