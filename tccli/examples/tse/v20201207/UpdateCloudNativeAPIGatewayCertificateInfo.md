**Example 1: 修改云原生网关证书信息**

修改云原生网关证书信息

Input: 

```
tccli tse UpdateCloudNativeAPIGatewayCertificateInfo --cli-unfold-argument  \
    --GatewayId abc \
    --Id abc \
    --Name abc \
    --BindDomains abc
```

Output: 
```
{
    "Response": {
        "RequestId": "abc"
    }
}
```

