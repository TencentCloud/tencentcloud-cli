**Example 1: 修改网关的转发配置**

修改网关的转发配置

Input: 

```
tccli tem ModifyGatewayIngress --cli-unfold-argument  \
    --EnvironmentId xx \
    --GatewayType clb \
    --GatewayName xx \
    --Name xx \
    --Rules.0.Protocol xx \
    --Rules.0.Host xx \
    --Rules.0.Http.Paths.0.Path xx \
    --Rules.0.Http.Paths.0.Backend.ServiceName xx \
    --Rules.0.Http.Paths.0.Backend.ServicePort 443 \
    --Tls.0.CertificateId xx \
    --Tls.0.Hosts xxx.com \
    --Tls.0.SecretName xx \
    --Mixed True \
    --RewriteType NONE
```

Output: 
```
{
    "Response": {
        "RequestId": "81f74023-563c-437d-abf7-8139449ef178",
        "Result": true
    }
}
```

