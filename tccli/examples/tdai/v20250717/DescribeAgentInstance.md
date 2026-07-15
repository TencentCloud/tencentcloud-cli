**Example 1: 查询智能体实例详情**



Input: 

```
tccli tdai DescribeAgentInstance --cli-unfold-argument  \
    --InstanceId agentins-efbt5y3h
```

Output: 
```
{
    "Response": {
        "AgentInstance": {
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
        },
        "RequestId": "a070f1a2-7538-5318-c843-6b47607aa78c"
    }
}
```

