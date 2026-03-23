**Example 1: 查询mcp server详情**

查询mcp server详情

Input: 

```
tccli apis DescribeMcpServer --cli-unfold-argument  \
    --InstanceID ins-9c4a1db3 \
    --ID mcp-8d5c4195
```

Output: 
```
{
    "Response": {
        "Data": {
            "AppID": 1300273807,
            "Uin": "700001136234",
            "InstanceID": "ins-9c4a1db3",
            "Name": "test",
            "Description": "",
            "LabelIDs": [],
            "CategoryIDs": [],
            "Mode": "proxy",
            "McpVersion": "2024-11-05",
            "WrapServices": [],
            "TargetSelect": "random",
            "TargetHosts": [
                {
                    "Host": "127.0.0.1:3002",
                    "Rank": 10
                }
            ],
            "HttpProtocolType": "http",
            "CheckTargetCertsError": false,
            "TargetPath": "/sse",
            "InvokeLimitConfigStatus": false,
            "InvokeLimitConfig": {
                "Type": "tokenBucket",
                "TokenBucketMaxNum": 20000,
                "TokenBucketRate": 1,
                "FunnelMaxNum": 20000,
                "FunnelRate": 1,
                "SlidingWindowMaxNum": 20000,
                "SlidingWindowSize": 1,
                "TimeWindow": 20000,
                "TimeWindowInterval": 1
            },
            "IpWhiteStatus": false,
            "IpWhiteConfig": {
                "Ips": [],
                "EffectType": "always",
                "EffectTimes": [],
                "Comment": ""
            },
            "IpBlackStatus": false,
            "IpBlackConfig": {
                "Ips": [],
                "EffectType": "always",
                "EffectTimes": [],
                "Comment": ""
            },
            "CustomHttpHost": "",
            "HttpHostType": "targetHost",
            "Timeout": 60,
            "ID": "mcp-8d5c4195",
            "Status": "disabled",
            "Url": "http://test.com/_llmsgw_/mcp?server=mcp-8d5c4195&paasid=app-83a7a4aa",
            "App": {
                "ID": "app-83a7a4aa",
                "Name": "test"
            },
            "Catalogs": [],
            "Labels": [],
            "ToolNum": -1,
            "CreateTime": "2025-05-20T08:24:18.702Z",
            "LastUpdateTime": "2025-05-20T08:42:05.916Z",
            "McpSecurityRulesVO": [
                {
                    "ID": "mr-2bdbbf32",
                    "Type": "sensitive_data_check",
                    "BodyType": "",
                    "IconType": "code",
                    "Name": "验证码",
                    "Description": "识别mcp服务调用过程中，响应参数可能存在的验证码",
                    "RiskLevel": "middle",
                    "VersionNumber": "20250509_v1",
                    "Status": "open",
                    "Act": "watch",
                    "SupportActs": [
                        "watch",
                        "desensitization",
                        "filter"
                    ]
                }
            ]
        },
        "RequestId": "7ecfb435-bc50-49b8-b206-4278f2b08db1"
    }
}
```

