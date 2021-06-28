**Example 1: 创建或者更新 Ingress 规则**

创建或者更新 Ingress 规则

Input: 

```
tccli tem ModifyIngress --cli-unfold-argument  \
    --SourceChannel 0 \
    --Ingress.Tls.0.CertificateId xx \
    --Ingress.Tls.0.Hosts xxx.com \
    --Ingress.Tls.0.SecretName xx \
    --Ingress.EksNamespace xx \
    --Ingress.Name xx \
    --Ingress.Rules.0.Protocol xx \
    --Ingress.Rules.0.Host xx \
    --Ingress.Rules.0.Http.Paths.0.Path xx \
    --Ingress.Rules.0.Http.Paths.0.Backend.ServiceName xx \
    --Ingress.Rules.0.Http.Paths.0.Backend.ServicePort 443 \
    --Ingress.ClbId xx \
    --Ingress.ClusterId xx \
    --Ingress.CreateTime xx \
    --Ingress.Vip xx \
    --Ingress.Mixed True \
    --Ingress.AddressIPVersion xx \
    --Ingress.NamespaceId xx
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

