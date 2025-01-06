**Example 1: 创建私有域名解析**



Input: 

```
tccli tcr CreateInternalEndpointDns --cli-unfold-argument  \
    --InstanceId tcr-dg284imq \
    --VpcId vpc-9iazgkcl \
    --EniLBIp 192.168.23.69 \
    --UsePublicDomain True \
    --RegionName ap-guangzhou \
    --RegionId 1
```

Output: 
```
{
    "Response": {
        "RequestId": "b6cf242e-a41f-4d1e-8a9c-16c6a0b8b326"
    }
}
```

