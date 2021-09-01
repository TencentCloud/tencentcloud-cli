**Example 1: 替换负载均衡实例关联的服务端证书**

指定新证书ID，替换服务端证书

Input: 

```
tccli clb ReplaceCertForLoadBalancers --cli-unfold-argument  \
    --OldCertificateId cuxw0123 \
    --Certificate.CertId cuxw4567
```

Output: 
```
{
    "Response": {
        "RequestId": "00ca7fca-90f1-47fe-a724-5d7e96d04633"
    }
}
```

