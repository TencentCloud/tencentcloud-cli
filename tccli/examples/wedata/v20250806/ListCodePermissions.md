**Example 1: 查询文件权限列表**



Input: 

```
tccli wedata ListCodePermissions --cli-unfold-argument  \
    --ProjectId 1464962169590902784 \
    --PageNumber 1 \
    --PageSize 10 \
    --Resource.ResourceType script \
    --Resource.ResourceId fcec3d4e-e099-4c26-9154-0745ee1a9895 \
    --Resource.ResourceIdForPath /cc1c8732-d398-43f8-b5cf-6e66b8258208/fcec3d4e-e099-4c26-9154-0745ee1a9895
```

Output: 
```
{
    "Response": {
        "Data": {
            "PageNumber": 1,
            "PageSize": 10,
            "Rows": [
                {
                    "DeleteAble": false,
                    "Privileges": [
                        "CAN_MANAGE"
                    ],
                    "Resource": {
                        "ResourceId": "fcec3d4e-e099-4c26-9154-0745ee1a9895",
                        "ResourceIdForPath": null,
                        "ResourceType": "script"
                    },
                    "RoleId": "308335260274237440",
                    "RoleType": "role"
                }
            ],
            "TotalCount": 3,
            "TotalPageNumber": null
        },
        "RequestId": "5eca8af5-9747-49fe-bf13-148444fa24ee"
    }
}
```

