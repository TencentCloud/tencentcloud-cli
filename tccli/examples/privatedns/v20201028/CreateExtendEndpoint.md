**Example 1: 创建转发目标为CLB的终端节点服务**

创建转发目标为CLB的终端节点服务

Input: 

```
tccli privatedns CreateExtendEndpoint --cli-unfold-argument  \
    --EndpointName 测试终端节点 \
    --EndpointRegion ap-guangzhou \
    --ForwardIp.AccessType CLB \
    --ForwardIp.Host 10.110.2.8 \
    --ForwardIp.Port 53 \
    --ForwardIp.IpNum 1 \
    --ForwardIp.VpcId vpc-xxxxxxx \
    --ForwardIp.SubnetId subnet-xxxxxxx
```

Output: 
```
{
    "Response": {
        "RequestId": "0a4303be-e127-4b90-a524-e87803b84ff1",
        "EndpointId": "eid-xxxxxxxxx",
        "EndpointName": "测试终端节点"
    }
}
```

