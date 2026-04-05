**Example 1: 成功调用**



Input: 

```
tccli wedata GetWorkspace --cli-unfold-argument  \
    --WorkspaceId 17622177773248536
```

Output: 
```
{
    "Response": {
        "Data": {
            "WorkspaceInfo": {
                "CreateTime": "2025-11-04 08:56:17",
                "Creator": {
                    "Nickname": "",
                    "Uin": "700002164618",
                    "UserName": ""
                },
                "Description": "",
                "ErrorReason": "",
                "Status": 1,
                "UpdateTime": "2025-11-04 08:56:17",
                "WorkspaceId": "17622177773248536",
                "WorkspaceName": "默认工作空间",
                "WorkspaceRegion": "ap-guangzhou"
            }
        },
        "RequestId": "9697d7ab-4ffb-45cb-8943-d53b8399052e"
    }
}
```

