**Example 1: 删除私有域名解析**



Input: 

```
tccli tcr DeleteInternalEndpointDns --cli-unfold-argument  \
    --InstanceId tcr-xxx \
    --VpcId vpc-xxx \
    --EniLBIp 1.1.1.1 \
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

