**Example 1: 创建私有域名解析**



Input: 

```
tccli tcr CreateInternalEndpointDns --cli-unfold-argument  \
    --InstanceId tcr-xxx \
    --EniLBIp 1.1.1.1 \
    --VpcId vpc-xxx \
    --UsePublicDomain false
```

Output: 
```
{
    "Response": {
        "RequestId": "xxxxxx"
    }
}
```

