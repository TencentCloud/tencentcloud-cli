**Example 1: 查询MCP Server模板列表**

模糊搜索模板

Input: 

```
tccli lighthouse DescribeMcpServerTemplates --cli-unfold-argument  \
    --Filters.0.Name name-description \
    --Filters.0.Values lighthouse \
    --Limit 10 \
    --Offset 0
```

Output: 
```
{
    "Response": {
        "McpServerTemplateSet": [
            {
                "Command": "bnB4IC15IGxpZ2h0aG91c2UtbWNwLXNlcnZlcg==",
                "CommunityUrl": "https://www.npmjs.com/package/lighthouse-mcp-server",
                "Description": "基于MCP协议的腾讯云Lighthouse MCP Server，借助大模型即可完成实例防火墙配置、实例检测、监控分析等常用功能。",
                "EnvSet": [
                    {
                        "Key": "TENCENTCLOUD_SECRET_ID",
                        "Value": "YOUR_TENCENT_SECRET_ID"
                    },
                    {
                        "Key": "TENCENTCLOUD_SECRET_KEY",
                        "Value": "YOUR_TENCENT_SECRET_KEY"
                    }
                ],
                "IconUrl": "https://cloudcache.tencent-cloud.com/qcloud/ui/static/other_external_resource/6e6c2ea3-301f-4ce2-8fd9-3952c6eb04b5.png",
                "Name": "腾讯云 Lighthouse MCP Server",
                "PlatformUrl": "https://console.cloud.tencent.com/cam/capi"
            }
        ],
        "RequestId": "3ac46471-af2f-458a-919b-bec201887d6b",
        "TotalCount": 1
    }
}
```

