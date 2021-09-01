**Example 1: 查询客户端状态**



Input: 

```
tccli tat DescribeAutomationAgentStatus --cli-unfold-argument  \
    --InstanceIds lhins-ar5wyn4x
```

Output: 
```
{
    "Response": {
        "RequestId": "520e7b93-904d-44de-a2dd-8e4c545be4ce",
        "AutomationAgentSet": [
            {
                "InstanceId": "lhins-ar5wyn4x",
                "Version": "0.1.0",
                "LastHeartbeatTime": "2020-11-16T12:05:44+00:00",
                "AgentStatus": "Online",
                "Environment": "Linux"
            }
        ],
        "TotalCount": 1
    }
}
```

