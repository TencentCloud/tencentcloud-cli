**Example 1: Replacing the server certificate associated with a CLB instance**

This example shows you how to replace a server certificate by specifying a certificate ID.

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

