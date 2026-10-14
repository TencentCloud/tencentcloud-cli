**Example 1: 成功**



Input: 

```
tccli iss DescribeVideoSnapshotConfig --cli-unfold-argument  \
    --ConfigId b8a**3***********************daafd74
```

Output: 
```
{
    "Response": {
        "Data": {
            "Callback": {
                "Token": "",
                "Url": "http:/****3*************callback"
            },
            "ConfigId": "b8ab03**********************7daafd74",
            "CreateTime": "2026-01-25 14:55:34",
            "FileExpires": 15,
            "Name": "截图配置1",
            "TemplateId": "144d8**********************3ed07f3d3",
            "Type": 1,
            "UpdateTime": "2026-01-25 15:12:03"
        },
        "RequestId": "854d322f-f794-4b5f-bda1-aa514020e9e4"
    }
}
```

