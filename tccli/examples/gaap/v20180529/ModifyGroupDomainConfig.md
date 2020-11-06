**Example 1: 配置通道组就近接入域名**



Input: 

```
tccli gaap ModifyGroupDomainConfig --cli-unfold-argument  \
    --GroupId lg-b7h4d02f \
    --DefaultDnsIp 1.1.1.1 \
    --AccessRegionList []
```

Output: 
```
{
    "Response": {
        "RequestId": "74b5f95c-e976-4f78-b2ee-aad49eb844c4"
    }
}
```

