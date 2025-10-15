**Example 1: 创建入站终端节点**

创建入站终端节点

Input: 

```
tccli privatedns CreateInboundEndpoint --cli-unfold-argument  \
    --EndpointName inbound \
    --EndpointRegion ap-guangzhou \
    --EndpointVpc vpc-ptyhb4st \
    --SubnetIp.0.SubnetId subnet-73kub9yu
```

Output: 
```
{
    "Response": {
        "EndpointId": "inbound-fad034d268",
        "EndpointName": "inbound",
        "RequestId": "3bef6b27-3b6a-476c-99f0-4781e95e1e20"
    }
}
```

