**Example 1: 查询工作空间用户组用户列表**



Input: 

```
tccli wedata ListWorkspaceGroupUsers --cli-unfold-argument  \
    --GroupId 17627618266798638
```

Output: 
```
{
    "Response": {
        "Data": {
            "Items": [
                {
                    "CreateTime": "1764141254909",
                    "Nickname": "micofywang",
                    "Uin": "700002219979",
                    "UpdateTime": "1764141254909",
                    "UserName": "micofywang"
                },
                {
                    "CreateTime": "1764141240450",
                    "Nickname": "tsinghu",
                    "Uin": "700002220257",
                    "UpdateTime": "1764141240450",
                    "UserName": "tsinghu"
                },
                {
                    "CreateTime": "1762914620187",
                    "Nickname": "jayshi",
                    "Uin": "700002226757",
                    "UpdateTime": "1763201933345",
                    "UserName": "jayshi"
                },
                {
                    "CreateTime": "1762914620179",
                    "Nickname": "member",
                    "Uin": "700002220464",
                    "UpdateTime": "1762937685421",
                    "UserName": "member"
                }
            ],
            "PageResponse": {
                "PageNumber": 1,
                "PageSize": 10,
                "TotalCount": 4,
                "TotalPageNumber": 1
            }
        },
        "RequestId": "42bb452b-f48e-48d0-9e67-b6f3414c2979"
    }
}
```

