**Example 1: 查询Agent信息**



Input: 

```
tccli lighthouse DescribeAgents --cli-unfold-argument  \
    --InstanceId lhins-ouit8fhb \
    --AgentIds lhagt-jhrmwkmt
```

Output: 
```
{
    "Response": {
        "AgentSet": [
            {
                "AgentContainerConfiguration": {
                    "AgentName": "echo-server2",
                    "Command": "",
                    "ContainerImage": "ealen/echo-server",
                    "Description": "Test agent for ginkgo integration test",
                    "Envs": [
                        {
                            "Key": "PORT",
                            "Value": "8000"
                        }
                    ],
                    "Volumes": []
                },
                "AgentId": "lhagt-jhrmwkmt",
                "AgentState": "RUNNING",
                "CreatedTime": "2025-10-24T08:47:30Z",
                "UpdatedTime": "2025-10-24T08:47:39Z"
            }
        ],
        "TotalCount": 1,
        "RequestId": "e07b9e13-4864-4da8-833c-520c538dface"
    }
}
```

