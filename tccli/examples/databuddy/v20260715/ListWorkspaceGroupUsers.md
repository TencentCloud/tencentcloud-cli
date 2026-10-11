**Example 1: ListWorkspaceGroupUsers**

查询工作空间用户组用户列表

Input: 

```
tccli databuddy ListWorkspaceGroupUsers --cli-unfold-argument  \
    --WorkspaceId 17623497097012366 \
    --GroupId 17667377941556921 \
    --NameKeywords brian \
    --UserUins 700002213764 \
    --OrderBys.0.Name CreateTime \
    --OrderBys.0.Direction DESC \
    --PageNumber 1 \
    --PageSize 10
```

Output: 
```
{
    "Response": {
        "Data": {
            "Items": [
                {
                    "CreateTime": "1768306785636",
                    "Nickname": "brian-dev",
                    "UpdateTime": "1783698994446",
                    "UserName": "brian-dev",
                    "UserUin": "700002213764"
                }
            ],
            "PageNumber": 1,
            "PageSize": 10,
            "TotalCount": 2,
            "TotalPageNumber": 1
        },
        "RequestId": "a9ad9ba2-680b-4b84-9e2d-150c7edceb33"
    }
}
```

