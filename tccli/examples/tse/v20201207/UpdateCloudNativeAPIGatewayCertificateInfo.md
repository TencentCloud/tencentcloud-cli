**Example 1: 修改云原生网关证书信息**

修改云原生网关证书信息

Input: 

```
tccli tse UpdateCloudNativeAPIGatewayCertificateInfo --cli-unfold-argument  \
    --GatewayId gateway-dde03767 \
    --Id 2a212560-220a-46f6-b139-3238eb8ea041 \
    --Name tencent \
    --BindDomains tencent.com
```

Output: 
```
{
    "Response": {
        "RequestId": "ffadafb6-545d-461c-ad8c-baa26c0f8955"
    }
}
```

