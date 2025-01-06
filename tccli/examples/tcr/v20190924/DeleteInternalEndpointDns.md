**Example 1: 删除私有域名解析**



Input: 

```
tccli tcr DeleteInternalEndpointDns --cli-unfold-argument  \
    --InstanceId tcr-dg284imq \
    --VpcId vpc-9iazgkcl \
    --EniLBIp 192.168.23.69 \
    --UsePublicDomain True \
    --RegionName ap-guangzhou
```

Output: 
```
{
    "Response": {
        "RequestId": "f63b71b9-196b-4648-a086-8a29c2bffc86"
    }
}
```

