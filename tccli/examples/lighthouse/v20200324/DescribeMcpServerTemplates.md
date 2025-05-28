**Example 1: 查询MCP Server模板列表**

限制返回结果最多为一项

Input: 

```
tccli lighthouse DescribeMcpServerTemplates --cli-unfold-argument  \
    --Filters.0.Name name-description \
    --Filters.0.Values map \
    --Limit 1
```

Output: 
```
{
    "Response": {
        "TotalCount": 1,
        "McpServerTemplateSet": [
            {
                "Name": "AMap",
                "Command": "bnB4IC15IEBtb2RlbGNvbnRleHRwcm90b2NvbC9tYXA=",
                "Description": "高德地图官网MCP Server",
                "IconUrl": "https://lbs.amap.com/favicon.ico",
                "CommunityUrl": "https://lbs.amap.com/api/mcp-server/summary",
                "PlatformUrl": "https://console.amap.com/dev/index",
                "EnvSet": [
                    {
                        "Key": "MAP_API_KEY",
                        "Value": "api_key_xxx_xxx"
                    }
                ]
            }
        ],
        "RequestId": "d8a6d860-c9bb-4390-b8da-fc976ffc7712"
    }
}
```

