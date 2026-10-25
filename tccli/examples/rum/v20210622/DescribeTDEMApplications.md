**Example 1: 查询应用列表**



Input: 

```
tccli rum DescribeTDEMApplications --cli-unfold-argument ```

Output: 
```
{
    "Response": {
        "ApplicationSet": [
            {
                "AppId": "app-9qPVpy9i2zF2",
                "CreatedAt": "2026-09-21 20:32:09",
                "Desc": "测试应用描述",
                "ExcludeIgnoredErrors": false,
                "InstanceId": "rum-LgSqrGWEdgsx",
                "InstanceName": "修改业务系统名称",
                "Name": "测试应用",
                "ProjectKey": "v2n3KR2s9axu",
                "Status": 2,
                "Type": "web"
            }
        ],
        "TotalCount": 2,
        "RequestId": "8f61090b-6a6d-435c-b738-13bf16ed249c"
    }
}
```

