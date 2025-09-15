**Example 1: 查询智能体实例列表**



Input: 

```
tccli tdai DescribeAgentInstances --cli-unfold-argument  \
    --InstanceId agentins-efbt5y3h \
    --InstanceName agentins-efbt5y3h \
    --AgentId agt-xpcn2t3e \
    --AgentName sqlAgent测试 \
    --AgentInternalName aid \
    --Status running \
    --Offset 0 \
    --Limit 10
```

Output: 
```
{
    "Response": {
        "Items": [
            {
                "InstanceId": "agentins-efbt5y3h",
                "InstanceName": "agentins-efbt5y3h",
                "AgentId": "agt-xpcn2t3e",
                "AgentName": "sqlAgent测试",
                "AgentInternalName": "aid",
                "AgentType": "chat",
                "AgentVersion": "v1.0.0",
                "Status": "running",
                "Parameters": [
                    {
                        "Key": "git_branch",
                        "Value": "master",
                        "ValueType": "string"
                    }
                ],
                "CreateTime": "2025-07-15 16:06:10",
                "UpdateTime": "2025-07-15 16:06:10"
            }
        ],
        "RequestId": "a070f1a2-7538-5318-c843-6b47607aa78c",
        "TotalCount": 1
    }
}
```

