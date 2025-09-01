**Example 1: 发起MCP Server部署**

发起MCP Server部署。

Input: 

```
tccli lighthouse StartMcpServerDeployments --cli-unfold-argument  \
    --McpServerProjectId lhmsp-axjdikig \
    --Name my-mcp-server \
    --Description This is a test MCP Server \
    --IconUrl https://example.com/icon.png \
    --CodeFiles.0.CosKey agent_generated/actived/12345/lhmsp-axjdikig/main.py \
    --CodeFiles.0.CodeSha256 1b4f0e9851971998e732078544c96b36c3d01cedf7caa332359d6f1d83567014 \
    --CodeFiles.1.CosKey agent_generated/actived/12345/lhmsp-axjdikig/requirements.txt \
    --CodeFiles.1.CodeSha256 60303ae22b998861bce3b28f33eec1be758a213c86c93c076dbe9f558c11c752 \
    --InstanceDeployments.0.Region ap-guangzhou \
    --InstanceDeployments.0.InstanceId lhins-lart4xxz
```

Output: 
```
{
    "Response": {
        "McpServerDeploymentSet": [
            {
                "McpServerDeploymentId": "lhmsd-axjdikig",
                "McpServerId": "lhms-abcdefgh",
                "McpServerName": "my-mcp-server",
                "InstanceId": "lhins-lart4xxz",
                "InstanceName": "green-lh-test",
                "Region": "ap-guangzhou",
                "State": "PENDING",
                "CreatedTime": "2023-06-13T13:55:53Z"
            }
        ],
        "RequestId": "e29e6e6a-6903-4eff-80d3-335f4a0a454c"
    }
}
```

