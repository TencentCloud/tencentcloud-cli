**Example 1: 分享嵌出、分享配置信息查询**



Input: 

```
tccli wedata ShareApplicationConfig --cli-unfold-argument  \
    --DashboardAccessKey 796335615169191936 \
    --WorkspaceId 17622177773248536
```

Output: 
```
{
    "Response": {
        "Data": {
            "DashboardAccessKey": "796335615169191936",
            "DashboardStatus": "PUBLISHED",
            "FileId": "796335615169191936",
            "ShareConfig": "{\"AccessType\":\"INVITED_ONLY\",\"Status\":\"PUBLISHED\"}"
        },
        "RequestId": "78ddcf54-1b69-43b7-92cb-349bae4bc59a"
    }
}
```

