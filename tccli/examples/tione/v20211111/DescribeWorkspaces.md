**Example 1: 查询工作空间列表**



Input: 

```
tccli tione DescribeWorkspaces --cli-unfold-argument  \
    --TiProjectId 1889353273052233728 \
    --Limit 2
```

Output: 
```
{
    "Response": {
        "RequestId": "6328c505-e6b7-40e1-9185-aaebd6f8310f",
        "TotalCount": 21,
        "Workspaces": [
            {
                "ActionType": [],
                "CreateTime": "",
                "Description": "",
                "Name": "默认空间",
                "TiProjectId": "0"
            },
            {
                "ActionType": [
                    "ModifyWorkspace",
                    "DeleteWorkspace"
                ],
                "CreateTime": "2025-11-24T18:32:39+08",
                "Description": "",
                "Name": "测试空间",
                "TiProjectId": "1889353273052233728"
            }
        ]
    }
}
```

