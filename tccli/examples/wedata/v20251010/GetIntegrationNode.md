**Example 1: 查询集成节点**



Input: 

```
tccli wedata GetIntegrationNode --cli-unfold-argument  \
    --Id 1 \
    --WorkspaceId test-project-001
```

Output: 
```
{
    "Response": {
        "Data": {
            "NodeInfo": {
                "AppId": "251436191",
                "Config": [],
                "ConnectionId": "62274",
                "CreateTime": "0",
                "CreatorUin": "700002164618",
                "Description": "读取",
                "ExtConfig": [],
                "Id": "1",
                "Name": "MySQL",
                "NodeType": "INPUT",
                "OperatorUin": "700002164618",
                "OwnerUin": "700002164618",
                "Schema": [
                    {
                        "Alias": "id",
                        "Category": "",
                        "Comment": "",
                        "Id": "1",
                        "Name": "id",
                        "Properties": [],
                        "Type": "int",
                        "Value": ""
                    }
                ],
                "TaskId": "314a06b9-19ea-459c-b613-871ab5b606ed",
                "UpdateTime": "0",
                "WorkspaceId": "test-project-001"
            },
            "SourceCheckFlag": false
        },
        "RequestId": "82f4f979-3b0d-4992-a828-0bc731b5e915"
    }
}
```

