**Example 1: 创建或者更新 Ingress 规则**

创建或者更新 Ingress 规则

Input: 

```
tccli tem ModifyIngress --cli-unfold-argument  \
    --Ingress.ClusterId cls-9lxt9ic2 \
    --Ingress.AddressIPVersion IPV4 \
    --Ingress.Name test-ingress-1 \
    --Ingress.Rules.0.Host  \
    --Ingress.Rules.0.Http.Paths.0.Path / \
    --Ingress.Rules.0.Http.Paths.0.Backend.ServiceName kubernetes \
    --Ingress.Rules.0.Http.Paths.0.Backend.ServicePort 443 \
    --Ingress.Tls.0.Hosts xxx.com \
    --Ingress.Tls.0.SecretName xxx
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

