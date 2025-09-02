**Example 1: 修改MCP Server信息**

修改指定MCP Server的信息。

Input: 

```
tccli lighthouse ModifyMcpServer --cli-unfold-argument  \
    --InstanceId lhins-5h3s0lht \
    --McpServerId lhms-p2dophob \
    --Name 腾讯云 Lighthouse MCP Server \
    --Command bnB4IC15IGxpZ2h0aG91c2UtbWNwLXNlcnZlcg== \
    --Description 基于MCP协议的腾讯云Lighthouse MCP Server，借助大模型即可完成实例防火墙配置、实例检测、监控分析等常用功能。 \
    --Envs.0.Key TENCENTCLOUD_SECRET_KEY \
    --Envs.0.Value MODIFIED_TENCENT_SECRET_KEY \
    --Envs.1.Key TENCENTCLOUD_SECRET_ID \
    --Envs.1.Value MODIFIED_TENCENT_SECRET_ID
```

Output: 
```
{
    "Response": {
        "RequestId": "54b97dbc-e8d3-45f0-b648-2934d76c1cf9"
    }
}
```

