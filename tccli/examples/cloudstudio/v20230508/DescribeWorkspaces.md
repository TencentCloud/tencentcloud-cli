**Example 1: 查询指定地域的工作空间**



Input: 

```
tccli cloudstudio DescribeWorkspaces --cli-unfold-argument ```

Output: 
```
{
    "Response": {
        "Data": [
            {
                "Cpu": 2,
                "CreateDate": "2025-05-29T01:18:07.000+00:00",
                "Description": "",
                "Icon": "https://cs-res-1258344699.file.myqcloud.com/workspace/assets/icons/all-in-one.svg",
                "Id": 36039,
                "LastOpsDate": "2025-05-29T01:18:07.000+00:00",
                "Memory": 4,
                "Name": "AllinOne-wqigru",
                "SpaceKey": "wqigru",
                "Status": "PENDING",
                "StatusReason": "",
                "VersionControlRef": "",
                "VersionControlUrl": "https://e.coding.net/coding-public/cloud-studio-samples/programming-language-demo.git",
                "WorkspaceType": "NORMAL"
            }
        ],
        "RequestId": "d3bd7a2d-caf9-4984-98b8-a94a14b52a95"
    }
}
```

