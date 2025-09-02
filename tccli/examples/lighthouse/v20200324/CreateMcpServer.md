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

