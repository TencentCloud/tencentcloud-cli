**Example 1: 创建codestudio文件权限**



Input: 

```
tccli wedata CreateCodePermissions --cli-unfold-argument  \
    --ProjectId 1460947878944567296 \
    --AuthorizePermissionObjects.0.Resource.ResourceType script \
    --AuthorizePermissionObjects.0.Resource.ResourceId 20d6fbdb-5122-49ad-a94e-ac182099e11e \
    --AuthorizePermissionObjects.0.Resource.ResourceIdForPath /20e60838-78e7-4619-9fb8-528e2d43e855/20d6fbdb-5122-49ad-a94e-ac182099e11e \
    --AuthorizePermissionObjects.0.AuthorizeSubjects.0.SubjectType user \
    --AuthorizePermissionObjects.0.AuthorizeSubjects.0.SubjectValues 100043755527 \
    --AuthorizePermissionObjects.0.AuthorizeSubjects.0.Privileges CAN_MANAGE
```

Output: 
```
{
    "Response": {
        "Data": [
            {
                "Item": "20d6fbdb-5122-49ad-a94e-ac182099e11e",
                "Reason": "Authorization successful",
                "Result": true
            }
        ],
        "RequestId": "a0e88cf1-fe5f-44a2-8795-fd2d11913b99"
    }
}
```

