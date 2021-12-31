**Example 1: 请求示例**



Input: 

```
tccli eiam ListUsersInOrgNode --cli-unfold-argument  \
    --OrgNodeId 7999987a-c9dc-4dd2-b3e2-b52f53317aa6 \
    --IncludeOrgNodeChildInfo true
```

Output: 
```
{
    "Response": {
        "RequestId": "123",
        "OrgNodeIdPath": "acbe4ea1-ea82-****-b979-c3b8be5c08d1",
        "OrgNodeChildUserInfo": [
            {
                "OrgNodeIdPath": "acbe4ea1-ea82-****-b979-c3b8be5c08d1/45892fcd-578e-43c1-a4e3-3f0ca9782fe4",
                "OrgNodeId": "45892fcd-578e-****-a4e3-3f0ca9782fe4",
                "UserInfo": [
                    {
                        "Status": "NOT_ENABLED",
                        "UserName": "3",
                        "Email": null,
                        "UserId": "e8cc68ca-****-492e-8770-b44d05111058",
                        "Phone": "+86-178****78787",
                        "DisplayName": "t1",
                        "DataSource": "SELF_CREATE"
                    }
                ],
                "TotalUserNum": 1,
                "OrgNodeNamePath": "根节点/企业1"
            },
            {
                "OrgNodeIdPath": "acbe4ea1-ea82-****-b979-c3b8be5c08d1/e161551b-2100-49f6-adf9-def5987ea8d9",
                "OrgNodeId": "e161551b-2100-49f6-adf9-def5987ea8d9",
                "UserInfo": [
                    {
                        "Status": "NOT_ENABLED",
                        "UserName": "1111111111111111111111111111111111111111",
                        "Email": "11884244298@qq.com",
                        "UserId": "29a94c4d-****-4352-82c0-1ac1cb546220",
                        "Phone": "+86-16****62134",
                        "DisplayName": "开发人员",
                        "DataSource": "SELF_CREATE"
                    },
                    {
                        "Status": "NOT_ENABLED",
                        "UserName": "reset",
                        "Email": "11****44298@qq.com",
                        "UserId": "c6762eef-a0dd-****-bff3-b2842da10089",
                        "Phone": "+86-134****2134",
                        "DisplayName": "开发人员x",
                        "DataSource": "SELF_CREATE"
                    }
                ],
                "TotalUserNum": 2,
                "OrgNodeNamePath": "根节点/组织2"
            }
        ],
        "OrgNodeId": "acbe4ea1-****-4d35-b979-c3b8be5c08d1",
        "UserInfo": [
            {
                "Status": "NOT_ENABLED",
                "UserName": "1",
                "Email": null,
                "UserId": "6138bb2c-****-4bf4-b617-ddf0a0ac14d8",
                "Phone": "+86-15****45454",
                "DisplayName": "aldenli",
                "DataSource": "SELF_CREATE"
            },
            {
                "Status": "NOT_ENABLED",
                "UserName": "11",
                "Email": "118****4298@qq.com",
                "UserId": "5c834ac5-****-47a3-a26a-e0a37a7f7306",
                "Phone": "+86-67464512134",
                "DisplayName": "开发人员",
                "DataSource": "SELF_CREATE"
            },
            {
                "Status": "NOT_ENABLED",
                "UserName": "re2",
                "Email": "11****44298@qq.com",
                "UserId": "70496920-f4de-****-9e16-a2b99c632753",
                "Phone": "+86-13****512566",
                "DisplayName": "开发人员x",
                "DataSource": "SELF_CREATE"
            }
        ],
        "TotalUserNum": 3,
        "OrgNodeNamePath": "根节点"
    }
}
```

