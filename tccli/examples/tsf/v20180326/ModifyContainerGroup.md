**Example 1: 修改容器部署组**



Input: 

```
tccli tsf ModifyContainerGroup --cli-unfold-argument  \
    --GroupId group-xxxxxxx \
    --AccessType 2 \
    --ProtocolPorts.0.Protocol TCP \
    --ProtocolPorts.0.Port 80 \
    --ProtocolPorts.0.TargetPort 8080 \
    --UpdateType 1 \
    --UpdateIvl 5 \
    --SubnetId 1
```

Output: 
```
{
    "Response": {
        "RequestId": "751eb910-9243-4c2a-b8d6-5d764442796e",
        "Result": true
    }
}
```

