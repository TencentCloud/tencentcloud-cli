**Example 1: 修改服务访问方式列表**



Input: 

```
tccli tem ModifyApplicationService --cli-unfold-argument  \
    --ApplicationId app-xxxxxx \
    --SourceChannel 0 \
    --EnvironmentId en-xxxxxx \
    --Service.Name svc-name-xxx \
    --Service.Ports 8080 \
    --Service.Yaml apiVersion: xxx \
    --Service.ApplicationName app-name-xxx \
    --Service.VersionName ver-name-xxx \
    --Service.ClusterIp 11.xx.xx.xx \
    --Service.ExternalIp 10.xx.xx.xx \
    --Service.Type CLUSTER \
    --Service.SubnetId subnet-xxx \
    --Service.LoadBalanceId lb-xxxxxx \
    --Service.PortMappings.0.Port 8080 \
    --Service.PortMappings.0.TargetPort 8080 \
    --Service.PortMappings.0.Protocol TCP \
    --Service.PortMappings.0.ServiceName svc-name-xxx \
    --Service.ServicePortMappingList.0.Type CLUSTER \
    --Service.ServicePortMappingList.0.ServiceName svc-name-xxx \
    --Service.ServicePortMappingList.0.ClusterIp 11.xx.xx.xx \
    --Service.ServicePortMappingList.0.ExternalIp 10.xx.xx.xx \
    --Service.ServicePortMappingList.0.SubnetId subnet-xxxxxx \
    --Service.ServicePortMappingList.0.VpcId vpc-xxxxxx \
    --Service.ServicePortMappingList.0.LoadBalanceId lb-xxxxxx \
    --Service.ServicePortMappingList.0.Yaml apiVersion: xxx \
    --Service.ServicePortMappingList.0.Ports 8080 \
    --Service.ServicePortMappingList.0.PortMappingItemList.0.Port 8080 \
    --Service.ServicePortMappingList.0.PortMappingItemList.0.TargetPort 8080 \
    --Service.ServicePortMappingList.0.PortMappingItemList.0.Protocol TCP \
    --Service.ServicePortMappingList.0.ExternalDomain ext.com.xxx \
    --Service.FlushAll True \
    --Service.EnableRegistryNextDeploy 0 \
    --Service.ApplicationId app-xxxxxx \
    --Service.AllIpDone True \
    --Service.ExternalDomain ext.com.xxx \
    --Data.Type CLUSTER \
    --Data.ServiceName svc-name-xxx \
    --Data.ClusterIp 11.xx.xx.xx \
    --Data.ExternalIp 10.xx.xx.xx \
    --Data.SubnetId subnet-xxxxxx \
    --Data.VpcId vpc-xxxxxx \
    --Data.LoadBalanceId lb-xxxxxx \
    --Data.Yaml apiVersion: xxx \
    --Data.Ports 8080 \
    --Data.PortMappingItemList.0.Port 8080 \
    --Data.PortMappingItemList.0.TargetPort 8080 \
    --Data.PortMappingItemList.0.Protocol TCP \
    --Data.ExternalDomain ext.com.xxx
```

Output: 
```
{
    "Response": {
        "Result": true,
        "RequestId": "asdc122-xxx-xxx-xxx"
    }
}
```

