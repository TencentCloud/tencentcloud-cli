**Example 1: 修改服务访问方式列表**



Input: 

```
tccli tem ModifyApplicationService --cli-unfold-argument  \
    --ApplicationId app-xxxxxx \
    --SourceChannel 0 \
    --EnvironmentId en-xxxxxx \
    --Service.Name abc \
    --Service.Ports 0 \
    --Service.Yaml abc \
    --Service.ApplicationName abc \
    --Service.VersionName abc \
    --Service.ClusterIp abc \
    --Service.ExternalIp abc \
    --Service.Type abc \
    --Service.SubnetId abc \
    --Service.LoadBalanceId abc \
    --Service.PortMappings.0.Port 0 \
    --Service.PortMappings.0.TargetPort 0 \
    --Service.PortMappings.0.Protocol abc \
    --Service.PortMappings.0.ServiceName abc \
    --Service.ServicePortMappingList.0.Type abc \
    --Service.ServicePortMappingList.0.ServiceName abc \
    --Service.ServicePortMappingList.0.ClusterIp abc \
    --Service.ServicePortMappingList.0.ExternalIp abc \
    --Service.ServicePortMappingList.0.SubnetId abc \
    --Service.ServicePortMappingList.0.VpcId abc \
    --Service.ServicePortMappingList.0.LoadBalanceId abc \
    --Service.ServicePortMappingList.0.Yaml abc \
    --Service.ServicePortMappingList.0.Ports 0 \
    --Service.ServicePortMappingList.0.PortMappingItemList.0.Port 0 \
    --Service.ServicePortMappingList.0.PortMappingItemList.0.TargetPort 0 \
    --Service.ServicePortMappingList.0.PortMappingItemList.0.Protocol abc \
    --Service.ServicePortMappingList.0.ExternalDomain abc \
    --Service.FlushAll True \
    --Service.EnableRegistryNextDeploy 0 \
    --Service.ApplicationId abc \
    --Service.AllIpDone True \
    --Service.ExternalDomain abc \
    --Data.Type abc \
    --Data.ServiceName abc \
    --Data.ClusterIp abc \
    --Data.ExternalIp abc \
    --Data.SubnetId abc \
    --Data.VpcId abc \
    --Data.LoadBalanceId abc \
    --Data.Yaml abc \
    --Data.Ports 0 \
    --Data.PortMappingItemList.0.Port 0 \
    --Data.PortMappingItemList.0.TargetPort 0 \
    --Data.PortMappingItemList.0.Protocol abc \
    --Data.ExternalDomain abc
```

Output: 
```
{
    "Response": {
        "Result": true,
        "RequestId": "xxx"
    }
}
```

