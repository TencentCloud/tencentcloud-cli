**Example 1: 应用页面权限列表**



Input: 

```
tccli lowcode DescribePermissionForAppPage --cli-unfold-argument  \
    --Role 1 \
    --EnvId env-001 \
    --WeAppId app-TJiOL2X9
```

Output: 
```
{
    "Response": {
        "Data": [
            {
                "PageName": "xx",
                "AccessAble": true,
                "PageId": "xx"
            }
        ],
        "RequestId": "xx"
    }
}
```

