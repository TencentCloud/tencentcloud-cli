**Example 1: 创建MCP Server**

创建一个新的MCP Server。

Input: 

```
tccli lighthouse CreateMcpServer --cli-unfold-argument  \
    --InstanceId lhins-lart4xxz \
    --Name map \
    --Command ZW5jb2RlZCBtY3Agc2VydmVyIGNvbW1hbmQ= \
    --Description 此MCP Server用于提供地图访问功能。 \
    --Envs.0.Key MAP_API_KEY \
    --Envs.0.Value api_key_xxx_xxx
```

Output: 
```
{
    "Response": {
        "McpServerId": "lhms-oartxxxz",
        "RequestId": "42582c39-52fd-4a00-8019-c3c995e8f9d6"
    }
}
```

