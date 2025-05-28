**Example 1: 修改MCP Server信息**

修改指定MCP Server的信息。

Input: 

```
tccli lighthouse ModifyMcpServer --cli-unfold-argument  \
    --InstanceId lhins-lart4xxz \
    --McpServerId lhms-oartxxxz \
    --Name map-new \
    --Command ZW5jb2RlZCBuZXcgY29tbWFuZA== \
    --Description 更新后的MCP Server备注。 \
    --Envs.0.Key MAP_API_KEY \
    --Envs.0.Value api_key_new
```

Output: 
```
{
    "Response": {
        "RequestId": "42582c39-52fd-4a00-8019-c3c995e8f9d6"
    }
}
```

