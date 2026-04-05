**Example 1: 查看工作空间成员**



Input: 

```
tccli wedata ListWorkspaceMembers --cli-unfold-argument  \
    --WorkspaceId 17636381753502681
```

Output: 
```
{
    "Response": {
        "Data": {
            "Items": [
                {
                    "Id": "600000561778",
                    "Name": "my_test",
                    "SubjectType": 1
                }
            ],
            "PageResponse": {
                "ExtendInfo": "",
                "PageNumber": 1,
                "PageSize": 10,
                "TotalCount": 3,
                "TotalPageNumber": 1
            }
        },
        "RequestId": "a2b516db-b8b2-457a-a93d-c47f46bcc6c3"
    }
}
```

