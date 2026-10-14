**Example 1: 成功**



Input: 

```
tccli iss ModifyVideoSnapshotConfig --cli-unfold-argument  \
    --ConfigId b8a************9****************fd74 \
    --Name 截图配置1 \
    --FileExpires 15
```

Output: 
```
{
    "Response": {
        "Data": {
            "Callback": {
                "Token": "",
                "Url": "http:***********************back"
            },
            "ConfigId": "b8a*************************7****d**",
            "CreateTime": "2026-01-25 14:55:34",
            "FileExpires": 15,
            "Name": "截图配置1",
            "TemplateId": "144****1*7*****************3ed**f3d3",
            "Type": 1,
            "UpdateTime": "2026-01-25 14:55:34"
        },
        "RequestId": "898d2032-7859-4f12-b41f-f1d2042b9b02"
    }
}
```

