**Example 1: GetMCPServerConfig**



Input: 

```
tccli wedata GetMCPServerConfig --cli-unfold-argument  \
    --WorkspaceId 17733709721325301 \
    --ServerKey b07faf3c1774342306676b07faf97
```

Output: 
```
{
    "Response": {
        "Data": {
            "ConfigData": "{\"mcpServers\": {\"wedata-mcp\": {\"url\": \"http://127.0.0.1:7995/cloudapi/application/appserver/v1/McpMessage\"}}}",
            "CreatedBy": "wedata",
            "CreatedOn": "1774342306000",
            "CreatedUser": "wedata",
            "Description": "你是 WeData 数据中台的智能助手，通过 MCP 协议与 WeData 平台交互。你可以调用以下工具完成数据管理任务：1. 数据目录（Catalog）：查询数据库、数据表、字段信息及数据血缘关系；2. 数据集成（Integration）：管理数据集成任务，查询任务状态和运行记录；3. 数据开发（Development）：管理工作流和任务，查询任务实例执行情况；4. 数据质量（Quality）：查询数据质量规则和监控结果；5. 数据安全（Security）：查询数据分类分级和脱敏策略。调用工具前请先通过 tools/list 获取可用工具列表，根据用户需求选择合适的工具。",
            "ErrorMessage": "",
            "Key": "b07faf3c1774342306676b07faf97",
            "ModifiedBy": "wedata",
            "ModifiedOn": "1774342306000",
            "ModifiedUser": "wedata",
            "RefResource": "",
            "ServerName": "官方数据库查询MCP",
            "ServerType": "sql",
            "ServerUrl": "https://mcp.wedataapp-dev.cloud.tencent.com/api/1.0/mcp/http/sql",
            "Status": "active",
            "ToolCount": 11,
            "Tools": [
                {
                    "Description": "分页获取数据目录（Catalog）列表，返回 Id、Name、Type、Status 等信息。对应 API：ListCatalogs（2025-10-10）",
                    "InputSchema": "{\"type\":\"object\",\"properties\":{\"WorkspaceId\":{\"type\":\"string\",\"description\":\"工作空间唯一 ID（必填）\"},\"MaxResults\":{\"type\":\"integer\",\"description\":\"最大结果条数（可选）\"},\"PageToken\":{\"type\":\"string\",\"description\":\"分页 token，由上次请求返回的 NextPageToken（可选）\"},\"Types\":{\"type\":\"string\",\"description\":\"catalog 类型过滤，逗号分隔，可选值：TABLE、MODEL、VOLUME（可选）\"}},\"required\":[\"WorkspaceId\"]}",
                    "Name": "ListCatalogs",
                    "OutputSchema": ""
                }
            ],
            "TransportType": "streamable-http",
            "WorkspaceId": "wedata"
        },
        "RequestId": "6c7508b3-0a91-4e9e-a6ed-223f906545e9"
    }
}
```

