**Example 1: 创建MCP Server**

创建一个新的MCP Server。

Input: 

```
tccli lighthouse CreateMcpServer --cli-unfold-argument  \
    --InstanceId lhins-5h3s0lht \
    --Name 腾讯云 Lighthouse MCP Server \
    --Command bnB4IC15IGxpZ2h0aG91c2UtbWNwLXNlcnZlcg== \
    --Description 基于MCP协议的腾讯云Lighthouse MCP Server，借助大模型即可完成实例防火墙配置、实例检测、监控分析等常用功能。 \
    --Envs.0.Key TENCENTCLOUD_SECRET_KEY \
    --Envs.0.Value YOUR_TENCENT_SECRET_KEY \
    --Envs.1.Key TENCENTCLOUD_SECRET_ID \
    --Envs.1.Value YOUR_TENCENT_SECRET_ID
```

Output: 
```
{
    "Response": {
        "McpServerId": "lhms-p2dophob",
        "RequestId": "54a37c92-9e77-4ba2-a791-925ae44f37f2"
    }
}
```

**Example 2: 创建MCP Server-指定传输类型**

演示如何创建一个指定传输类型的MCP Server

Input: 

```
tccli lighthouse CreateMcpServer --cli-unfold-argument  \
    --InstanceId lhins-ah48gaor \
    --Name Sequential Thinking \
    --Command bnB4IC15IEBtb2RlbGNvbnRleHRwcm90b2NvbC9zZXJ2ZXItc2VxdWVudGlhbC10aGlua2luZw== \
    --Envs.0.Key TEST_ENV_KEY \
    --Envs.0.Value TEST_ENV_VALUE \
    --TransportType STREAMABLE_HTTP
```

Output: 
```
{
    "Response": {
        "McpServerId": "lhms-9v3z57px",
        "RequestId": "9b58cd17-6586-404f-ac93-7b2913024080"
    }
}
```

