**Example 1: 分享嵌出、用户空间信息查询**



Input: 

```
tccli wedata ShareWorkspaceInfo --cli-unfold-argument  \
    --WorkspaceId 17622177773248537 \
    --DashboardAccessKey 796335615169191936
```

Output: 
```
{
    "Response": {
        "Data": {
            "InWorkspace": false,
            "WorkspaceId": "17622177773248537"
        },
        "RequestId": "86a8adff-6407-45bf-a0f7-4518302014db"
    }
}
```

