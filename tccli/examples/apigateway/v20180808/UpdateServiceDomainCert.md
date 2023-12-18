**Example 1: UpdateServiceDomainCert**



Input: 

```
tccli apigateway UpdateServiceDomainCert --cli-unfold-argument  \
    --CloudCertId xxxx \
    --ServiceDomains.0.ServiceId service-xxxx \
    --ServiceDomains.0.Domain www.xxxx.com
```

Output: 
```
{
    "Response": {
        "RequestId": "c5168a22-722f-431d-8128-2606e8144374"
    }
}
```

