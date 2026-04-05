**Example 1: 发布共享模式仪表盘**

发布仪表盘

Input: 

```
tccli wedata UpdateApplicationDashboardStatus --cli-unfold-argument  \
    --WorkspaceId 17678671667189298 \
    --AccessKey 798652297072988160 \
    --DashboardVersion 0 \
    --Status PUBLISHED \
    --PublishStrategy {"DataPermission":"SHARE"}
```

Output: 
```
{
    "Response": {
        "Data": {
            "AccessKey": "798652297072988160",
            "DashboardVersion": 67,
            "PublishTime": "1768988414014"
        },
        "RequestId": "3daa6dcf-2f3d-47c8-a844-48560aae8fa2"
    }
}
```

