**Example 1: 创建Agent**



Input: 

```
tccli lighthouse CreateAgents --cli-unfold-argument  \
    --InstanceId lhins-49mqny0l \
    --Containers.0.ContainerImage ealen/echo-server \
    --Containers.0.AgentName vior \
    --Containers.0.Envs.0.Key PORT \
    --Containers.0.Envs.0.Value 8080
```

Output: 
```
{
    "Response": {
        "AgentIdSet": [
            "lhagt-kl8o8yhd"
        ],
        "RequestId": "2d8a6a53-165e-4a08-be23-63dac96e492e"
    }
}
```

