**Example 1: 创建智能体实例**



Input: 

```
tccli tdai CreateAgentInstance --cli-unfold-argument  \
    --AgentId agt-xpcn2t3e \
    --AgentVersion v1.0.0.0 \
    --InstanceName agentins-efbt5y3h \
    --Parameters.0.Key git_branch \
    --Parameters.0.Value master \
    --Parameters.0.ValueType string
```

Output: 
```
{
    "Response": {
        "RequestId": "3c140219-cfe9-470e-b241-907877d6fb03",
        "InstanceId": "agentins-efbt5y3h",
        "InstanceName": "agentins-efbt5y3h"
    }
}
```

