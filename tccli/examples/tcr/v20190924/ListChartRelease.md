**Example 1: 查询Chart仓库信息列表**

展示Harbor Chart 仓库列表

Input: 

```
tccli tcr ListChartRelease --cli-unfold-argument  \
    --Limit 20 \
    --NameSpaceName chartns \
    --RepositoryName chartRepo \
    --RegistryId tcr-xxx \
    --Offset 0 \
    --All True
```

Output: 
```
{
    "Response": {
        "RequestId": "d76f7a1b-d9e9-4454-b95b",
        "Charts": [
            {
                "Name": "test",
                "Version": "v1.0.0",
                "Description": "activity-apply",
                "ApiVersion": "v1",
                "AppVersion": "1.0.1",
                "UrlList": [
                    "charts/activity-apply-v1.0.1.tgz"
                ],
                "Created": "2021-01-20T07:04:22Z",
                "Digest": "8b7349239f79e5d7831a1b13csasaxaf2812c29df80"
            }
        ],
        "TotalCount": 1
    }
}
```

