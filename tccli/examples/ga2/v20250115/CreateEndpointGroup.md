**Example 1: 创建终端节点组**



Input: 

```
tccli ga2 CreateEndpointGroup --cli-unfold-argument  \
    --GlobalAcceleratorId ga-80bzejka \
    --ListenerId lsr-kzjzfs7n \
    --EndpointGroupType DEFAULT \
    --EndpointGroupConfiguration.Name group-1 \
    --EndpointGroupConfiguration.EndpointGroupRegion ap-guangzhou \
    --EndpointGroupConfiguration.Description description \
    --EndpointGroupConfiguration.EndpointConfigurations.0.EndpointType CustomDomain \
    --EndpointGroupConfiguration.EndpointConfigurations.0.EndpointService www.aaa.com \
    --EndpointGroupConfiguration.EndpointConfigurations.0.Weight 10 \
    --EndpointGroupConfiguration.EnableHealthCheck True \
    --EndpointGroupConfiguration.ConnectTimeout 10 \
    --EndpointGroupConfiguration.HealthCheckInterval 5 \
    --EndpointGroupConfiguration.UnhealthyThreshold 10 \
    --EndpointGroupConfiguration.HealthyThreshold 10 \
    --EndpointGroupConfiguration.CheckType HTTP \
    --EndpointGroupConfiguration.CheckPort 12 \
    --EndpointGroupConfiguration.ContextType context \
    --EndpointGroupConfiguration.CheckSendContext context \
    --EndpointGroupConfiguration.CheckRecvContext context \
    --EndpointGroupConfiguration.CheckDomain www.ccc.com \
    --EndpointGroupConfiguration.CheckPath /url1
```

Output: 
```
{
    "Response": {
        "RequestId": "a6e9b84a-fa0f-4db7-820e-3a268871ec28",
        "EndpointGroupId": "epg-agq25w5q",
        "TaskId": "c6fc23d3-2b36-4262-89f9-1c0ab634e44c"
    }
}
```

