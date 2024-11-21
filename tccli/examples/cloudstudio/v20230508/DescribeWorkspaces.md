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
                "Description": "this is a description",
                "WorkspaceType": "NORMAL",
                "CreateDate": "2022-06-10T06:55:45Z",
                "Icon": "https://cs-res-1258344699.file.myqcloud.com/workspace/assets/icons/all-in-one.svg",
                "StatusReason": "OK",
                "VersionControlUrl": "git@github.com:koajs/koa.git",
                "VersionControlRef": "refs/heads/main",
                "Cpu": 2,
                "Memory": 4
            }
        ],
        "RequestId": "ff57bfab-60d0-47ce-883c-f5230245636a"
    }
}
```

