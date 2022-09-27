**Example 1: 修改服务访问方式列表**



Input: 

```
tccli tem ModifyApplicationService --cli-unfold-argument  \
    --SourceChannel 0 \
    --ApplicationId xx \
    --Service.ApplicationName xx \
    --Service.ExternalIp xx \
    --Service.Name xx \
    --Service.ApplicationId xx \
    --Service.AllIpDone True \
    --Service.PortMappings.0.Protocol xx \
    --Service.PortMappings.0.ServiceName xx \
    --Service.PortMappings.0.TargetPort 0 \
    --Service.PortMappings.0.Port 0 \
    --Service.Yaml xx \
    --Service.LoadBalanceId xx \
    --Service.ServicePortMappingList.0.ExternalIp xx \
    --Service.ServicePortMappingList.0.VpcId xx \
    --Service.ServicePortMappingList.0.PortMappingItemList.0.Protocol xx \
    --Service.ServicePortMappingList.0.PortMappingItemList.0.TargetPort 0 \
    --Service.ServicePortMappingList.0.PortMappingItemList.0.Port 0 \
    --Service.ServicePortMappingList.0.Yaml xx \
    --Service.ServicePortMappingList.0.LoadBalanceId xx \
    --Service.ServicePortMappingList.0.ServiceName xx \
    --Service.ServicePortMappingList.0.ClusterIp xx \
    --Service.ServicePortMappingList.0.SubnetId xx \
    --Service.ServicePortMappingList.0.Type xx \
    --Service.ServicePortMappingList.0.Ports 0 \
    --Service.VersionName xx \
    --Service.ClusterIp xx \
    --Service.SubnetId xx \
    --Service.Type xx \
    --Service.Ports 0 \
    --Service.EnableRegistryNextDeploy 0 \
    --Service.FlushAll True \
    --EnvironmentId xx
```

Output: 
```
{
    "Response": {
        "Result": true,
        "RequestId": "xx"
    }
}
```

