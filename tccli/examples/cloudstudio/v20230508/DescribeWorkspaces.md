**Example 1: 获取当前用户工作空间列表**

获取当前用户工作空间列表

Input: 

```
tccli cloudstudio DescribeWorkspaces --cli-unfold-argument ```

Output: 
```
{
    "Response": {
        "Data": [
            {
                "Id": 9,
                "Name": "open_api_test-1",
                "SpaceKey": "ryvzki",
                "Status": "CREATING",
                "LastOpsDate": "2022-06-10T06:55:45Z",
                "Description": "",
                "WorkspaceType": "NORMAL",
                "CreateDate": "2022-06-10T06:55:45Z",
                "VersionControlUrl": "",
                "VersionControlRef": "",
                "Cpu": 0,
                "Memory": 0
            }
        ],
        "RequestId": "ff57bfab-60d0-47ce-883c-f5230245636a"
    }
}
```

