**Example 1: 成功**



Input: 

```
tccli iss CreateVideoSnapshotConfig --cli-unfold-argument  \
    --Name 配置1 \
    --TemplateId 144*************************e****3d3 \
    --FileExpires 7 \
    --Callback.Url http://*********************back
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
            "ConfigId": "b8a*****************************fd74",
            "CreateTime": "2026-01-25 14:55:34",
            "FileExpires": 7,
            "Name": "配置1",
            "TemplateId": "144****************************7f3d3",
            "Type": 1,
            "UpdateTime": "2026-01-25 14:55:34"
        },
        "RequestId": "369e1974-9d68-4a5b-aa68-83629eed416a"
    }
}
```

