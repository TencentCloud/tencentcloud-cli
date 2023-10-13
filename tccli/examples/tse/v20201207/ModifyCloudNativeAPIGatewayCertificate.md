**Example 1: 更新云原生网关证书**

更新云原生网关证书

Input: 

```
tccli tse ModifyCloudNativeAPIGatewayCertificate --cli-unfold-argument  \
    --GatewayId gateway-9abf3b79 \
    --Key -----BEGIN PRIVATE KEY-----
MIGHAgEAMBMGByqGSM49AgEG-END PRIVATE KEY----- \
    --Crt -----BEGIN CERTIFICATE-----
MIIBpTCCAUugAwIBAgIUVHl/M-----END CERTIFICATE----- \
    --CertId 8RTlvcjR \
    --Id f9a5d230-4fa6-4f45-86c3-c5f49d6ffc83 \
    --CertSource ssl
```

Output: 
```
{
    "Response": {
        "RequestId": "69515cd4-2ff3-45f8-a311-7f2d84cd4e0b"
    }
}
```

