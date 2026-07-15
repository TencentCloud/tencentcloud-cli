**Example 1: 监听器绑定扩展证书**



Input: 

```
tccli alb AssociateListenerAdditionalCertificates --cli-unfold-argument  \
    --CertificateIds Fm8Wp7x8 \
    --ListenerId lst-d9p3k7wa \
    --LoadBalancerId alb-f8q2xk9m
```

Output: 
```
{
    "Response": {
        "RequestId": "3b848733-70e5-4558-ae39-4b9938eb7609"
    }
}
```

