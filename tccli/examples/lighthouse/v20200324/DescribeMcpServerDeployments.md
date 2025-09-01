**Example 1: 查询MCP Server部署记录**

查询MCP Server部署记录。

Input: 

```
tccli lighthouse DescribeMcpServerDeployments --cli-unfold-argument  \
    --Limit 10 \
    --Offset 0
```

Output: 
```
{
    "Response": {
        "McpServerDeploymentSet": [
            {
                "McpServerDeploymentId": "lhdeploy-abcd1234",
                "McpServerId": "lhms-oartxxxz",
                "McpServerName": "My Weather App",
                "InstanceId": "lhins-lart4xxz",
                "InstanceName": "green-lh-test",
                "Region": "ap-guangzhou",
                "State": "RUNNING",
                "CreatedTime": "2025-06-24T18:00:00Z"
            }
        ],
        "TotalCount": 10,
        "RequestId": "e29e6e6a-6903-4eff-80d3-335f4a0a454c"
    }
}
```

