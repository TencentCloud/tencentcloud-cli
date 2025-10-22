**Example 1: 查询安全规则**

查询安全规则

Input: 

```
tccli apis DescribeMcpSecurityRule --cli-unfold-argument  \
    --ID mr-1f32be6a \
    --InstanceID ins-9c4a1db3
```

Output: 
```
{
    "Response": {
        "Data": {
            "AppID": 1300273807,
            "BodyType": "text",
            "BuildIn": true,
            "ByPass": "close",
            "Contents": [
                {
                    "Content": "",
                    "FunctionType": "mcpResponseBodyFilter",
                    "SwitchMs": false
                }
            ],
            "CreateTime": "2025-05-20T06:41:16.539Z",
            "DefaultStatus": "close",
            "Description": "识别mcp服务调用过程中，响应参数文本信息中可能涉及到的安全合规问题",
            "ID": "mr-1f32be6a",
            "IconType": "text",
            "InstanceID": "ins-9c4a1db3",
            "Name": "文本内容安全检测",
            "RiskLevel": "high",
            "SupportActs": [
                "watch",
                "intercept"
            ],
            "SupportToolBind": false,
            "Type": "tencent_content_security_check",
            "Uin": "700001136234",
            "UpdateTime": "2025-05-20T06:42:02.402Z",
            "UseCount": 0,
            "VersionNumber": "20250509_v1"
        },
        "RequestId": "5adb40d7-25a9-46a1-834f-a834c3b6547a"
    }
}
```

