**Example 1: 取消证书订单**



Input: 

```
tccli ssl CancelCertificateOrder --cli-unfold-argument  \
    --CertificateId abcb1234
```

Output: 
```
{
    "Response": {
        "CertificateId": "abcb1234",
        "RequestId": "9b397ac6-7d01-4fbc-8acc-52dd6ff0877b"
    }
}
```

