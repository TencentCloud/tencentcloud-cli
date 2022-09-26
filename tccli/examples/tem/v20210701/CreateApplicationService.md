**Example 1: 新增访问方式**



Input: 

```
tccli tem CreateApplicationService --cli-unfold-argument  \
    --SourceChannel 0 \
    --ApplicationId xx \
    --Service.ExternalIp xx \
    --Service.VpcId xx \
    --Service.PortMappingItemList.0.Protocol xx \
    --Service.PortMappingItemList.0.TargetPort 0 \
    --Service.PortMappingItemList.0.Port 0 \
    --Service.Yaml xx \
    --Service.LoadBalanceId xx \
    --Service.ServiceName xx \
    --Service.ClusterIp xx \
    --Service.SubnetId xx \
    --Service.Type xx \
    --Service.Ports 0 \
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

