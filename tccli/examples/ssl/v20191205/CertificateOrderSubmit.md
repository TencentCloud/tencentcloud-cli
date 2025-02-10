**Example 1: 付费证书提交订单**

付费证书提交订单

Input: 

```
tccli ssl CertificateOrderSubmit --cli-unfold-argument  \
    --CertId abc \
    --DeleteDnsAutoRecord 1 \
    --VerifyType abc
```

Output: 
```
{
    "Response": {
        "OrderId": "abc",
        "Status": 1,
        "IsAudited": true,
        "RequestId": "abc"
    }
}
```

