**Example 1: 查询MCP Server列表**

查询指定实例下的MCP Server列表。

Input: 

```
tccli lighthouse DescribeMcpServers --cli-unfold-argument  \
    --InstanceId lhins-lart4xxz \
    --McpServerIds lhms-oartxxxz \
    --Limit 20 \
    --Offset 0
```

Output: 
```
{
    "Response": {
        "McpServerSet": [
            {
                "McpServerId": "lhms-oartxxxz",
                "Name": "map",
                "IconUrl": "https://example.com/icon.png",
                "Command": "ZW5jb2RlZCBtY3Agc2VydmVyIGNvbW1hbmQ=",
                "State": "RUNNING",
                "ServerUrl": "http://127.0.0.1/map/sse",
                "Config": "{\"mcpServers\":{\"map\":{\"url\":\"http://127.0.0.1/map/sse\"}}}",
                "Description": "此MCP Server用于提供地图访问功能。",
                "CreatedTime": "2025-05-09T17:50:14Z",
                "UpdatedTime": "2025-05-09T17:50:14Z",
                "EnvSet": [
                    {
                        "Key": "MAP_API_KEY",
                        "Value": "api_key_xxx_xxx"
                    }
                ]
            }
        ],
        "TotalCount": 1,
        "RequestId": "42582c39-52fd-4a00-8019-c3c995e8f9d6"
    }
}
```

