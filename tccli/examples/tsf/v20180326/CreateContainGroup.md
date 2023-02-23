**Example 1: 创建容器部署组**

创建容器部署组

Input: 

```
tccli tsf CreateContainGroup --cli-unfold-argument  \
    --CpuRequest 0.25 \
    --MemRequest 128 \
    --InstanceNum 1 \
    --ApplicationId application-xxxxxxx \
    --GroupName consumer \
    --NamespaceId namespace-xxxxxxx \
    --ClusterId cls-xxxxxxx \
    --AccessType 2 \
    --ProtocolPorts.0.Protocol TCP \
    --ProtocolPorts.0.Port 90 \
    --ProtocolPorts.0.TargetPort 90
```

Output: 
```
{
    "Response": {
        "RequestId": "39bb8e88-1ccd-4204-9f9e-56804c980a31",
        "Result": "group-xxxxxxx（已废弃，请使用 CreateGroup 和 DeployContainerGroup 创建和部署容器部署组）"
    }
}
```

