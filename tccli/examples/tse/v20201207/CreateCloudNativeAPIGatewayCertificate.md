**Example 1: 创建客户端证书示例**



Input: 

```
tccli tse CreateCloudNativeAPIGatewayCertificate --cli-unfold-argument  \
    --GatewayId gateway-9a766f25 \
    --CertId ZTQSzGeI \
    --Name client-cert-test \
    --CertType SVR \
    --CertUsage CLIENT
```

Output: 
```
{
    "Response": {
        "Result": {
            "Id": "386ead60-b5b9-454f-95cd-b1aed1c092b0"
        },
        "RequestId": "eb569733-5b0c-462f-9101-9bb471fddf85"
    }
}
```

