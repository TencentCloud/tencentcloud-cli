**Example 1: 新增访问方式**



Input: 

```
tccli tem CreateApplicationService --cli-unfold-argument  \
    --ApplicationId app-xxxxxx \
    --SourceChannel 0 \
    --EnvironmentId en-xxxxxx \
    --Service.Type VPC \
    --Service.ServiceName svc-name-xxx \
    --Service.ClusterIp 10.xx.xx.xx \
    --Service.ExternalIp 10.xx.xx.xx \
    --Service.SubnetId subnet-xxxxxx \
    --Service.VpcId vpc-xxxxxx \
    --Service.LoadBalanceId 10.xx.xx.xx \
    --Service.Yaml yaml-apiVersion-xxx \
    --Service.Ports 0 \
    --Service.PortMappingItemList.0.Port 8080 \
    --Service.PortMappingItemList.0.TargetPort 8080 \
    --Service.PortMappingItemList.0.Protocol TCP \
    --Service.ExternalDomain ext.domain.xxx
```

Output: 
```
{
    "Response": {
        "Result": true,
        "RequestId": "xx-xxx-xxx"
    }
}
```

