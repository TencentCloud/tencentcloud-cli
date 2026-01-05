**Example 1: 查询app mcp关联列表**



Input: 

```
tccli apis DescribeAgentAppMcpServers --cli-unfold-argument  \
    --Limit 10 \
    --Offset 0 \
    --InstanceID ins-a7af1980 \
    --AgentAppIDs aga-05b85106 \
    --McpServerIDs mcp-2fc41d77
```

Output: 
```
{
    "Response": {
        "Data": {
            "Items": [
                {
                    "AgentCredentialID": "",
                    "AgentCredentialVO": {
                        "AppID": 0,
                        "Content": {
                            "Headers": [],
                            "STSService": "",
                            "STSSystem": ""
                        },
                        "CreateTime": "0001-01-01T00:00:00Z",
                        "ID": "",
                        "InstanceID": "",
                        "LastUpdateTime": "0001-01-01T00:00:00Z",
                        "Name": "",
                        "RelateAgentAppNum": 0,
                        "RelateMcpServerNum": 0,
                        "Status": "",
                        "Type": "",
                        "Uin": ""
                    },
                    "ID": "aga-05b85106",
                    "McpServerVO": {
                        "AppID": 1300273807,
                        "Catalogs": null,
                        "CategoryIDs": [],
                        "CheckTargetCertsError": false,
                        "CreateTime": "2025-08-07T09:55:58.696Z",
                        "CustomHttpHost": "",
                        "Description": "testmcp",
                        "HttpHostType": "targetHost",
                        "HttpProtocolType": "http",
                        "ID": "mcp-2fc41d77",
                        "InstanceID": "ins-a7af1980",
                        "InvokeLimitConfig": {
                            "FunnelMaxNum": 20000,
                            "FunnelRate": 1,
                            "SlidingWindowMaxNum": 20000,
                            "SlidingWindowSize": 1,
                            "TimeWindow": 20000,
                            "TimeWindowInterval": 1,
                            "TokenBucketMaxNum": 20000,
                            "TokenBucketRate": 1,
                            "Type": "tokenBucket"
                        },
                        "InvokeLimitConfigStatus": false,
                        "IpBlackConfig": {
                            "Comment": "",
                            "EffectTimes": [],
                            "EffectType": "always",
                            "Ips": []
                        },
                        "IpBlackStatus": false,
                        "IpWhiteConfig": {
                            "Comment": "",
                            "EffectTimes": [],
                            "EffectType": "always",
                            "Ips": []
                        },
                        "IpWhiteStatus": false,
                        "LabelIDs": [],
                        "Labels": null,
                        "LastUpdateTime": "2025-12-04T06:07:53.241Z",
                        "McpSecurityRulesVO": [],
                        "McpVersion": "2024-11-05",
                        "Mode": "wrap",
                        "Name": "testmcp",
                        "PluginConfigs": [],
                        "RelateAgentAppNum": 0,
                        "Status": "normal",
                        "TargetHosts": [],
                        "TargetPath": "/",
                        "TargetSelect": "random",
                        "Timeout": 60,
                        "ToolConfigs": [],
                        "ToolMessage": "",
                        "ToolNum": 0,
                        "Tools": [],
                        "Uin": "700001136234",
                        "Url": "",
                        "UrlObj": {
                            "SSEUrl": "http://10.0.0.4/_llmsgw_/sse/aga-05b85106/mcp-2fc41d77",
                            "StreamAbleUrl": "http://10.0.0.4/_llmsgw_/mcp/aga-05b85106/mcp-2fc41d77"
                        },
                        "WrapPaasID": "app-be27914b",
                        "WrapServices": [
                            "svr-7e7f07e8"
                        ]
                    },
                    "NeedAuth": false,
                    "RelateTime": "2025-12-02T03:59:02.13Z",
                    "SSEResourceIdentifier": ""
                }
            ],
            "Total": 1
        },
        "RequestId": "4958f16e-4ab8-4429-8ad5-167f6b25799b"
    }
}
```

