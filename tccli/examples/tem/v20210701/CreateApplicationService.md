**Example 1: 新增访问方式**



Input: 

```
tccli tem CreateApplicationService --cli-unfold-argument  \
    --ApplicationId app-xxxxxx \
    --SourceChannel 0 \
    --EnvironmentId en-xxxxxx \
    --Service.Type VPC \
    --Service.ServiceName abc \
    --Service.ClusterIp abc \
    --Service.ExternalIp abc \
    --Service.SubnetId abc \
    --Service.VpcId abc \
    --Service.LoadBalanceId abc \
    --Service.Yaml abc \
    --Service.Ports 0 \
    --Service.PortMappingItemList.0.Port 0 \
    --Service.PortMappingItemList.0.TargetPort 0 \
    --Service.PortMappingItemList.0.Protocol abc \
    --Service.ExternalDomain abc
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

