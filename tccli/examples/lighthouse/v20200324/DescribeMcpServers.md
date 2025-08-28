**Example 1: 查询MCP Server列表**

查询指定实例下的MCP Server列表。

Input: 

```
tccli lighthouse DescribeMcpServers --cli-unfold-argument  \
    --InstanceId lhins-5h3s0lht \
    --McpServerIds lhms-p2dophob \
    --Limit 10 \
    --Offset 0
```

Output: 
```
{
    "Response": {
        "InstanceId": "lhins-5h3s0lht",
        "InstanceName": "ai mcp server test",
        "McpServerSet": [
            {
                "Command": "bnB4IC15IGxpZ2h0aG91c2UtbWNwLXNlcnZlcg==",
                "Config": "{\"mcpServers\":{\"腾讯云 Lighthouse MCP Server\":{\"url\":\"http://1.14.57.202/lhms-p2dophob/sse\"}}}",
                "CreatedTime": "2025-08-27T07:33:14Z",
                "Description": "基于MCP协议的腾讯云Lighthouse MCP Server，借助大模型即可完成实例防火墙配置、实例检测、监控分析等常用功能。",
                "EnvSet": [
                    {
                        "Key": "TENCENTCLOUD_SECRET_KEY",
                        "Value": "**********"
                    },
                    {
                        "Key": "TENCENTCLOUD_SECRET_ID",
                        "Value": "**********"
                    }
                ],
                "IconUrl": "https://cloudcache.tencent-cloud.com/qcloud/ui/static/other_external_resource/6e6c2ea3-301f-4ce2-8fd9-3952c6eb04b5.png",
                "McpServerId": "lhms-p2dophob",
                "McpServerType": "PUBLIC_PACKAGE",
                "Name": "腾讯云 Lighthouse MCP Server",
                "ServerUrl": "http://1.14.57.202/lhms-p2dophob/sse",
                "State": "RUNNING",
                "UpdatedTime": "2025-08-27T07:37:43Z"
            }
        ],
        "RequestId": "fe83a82b-967c-4f58-89d2-9ee20f9dafc5",
        "TotalCount": 1
    }
}
```

