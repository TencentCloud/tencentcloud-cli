**Example 1: 付费证书提交订单**

付费证书提交订单

Input: 

```
tccli ssl CertificateOrderSubmit --cli-unfold-argument  \
    --CertId Dsqef134 \
    --DeleteDnsAutoRecord 1 \
    --VerifyType DNS
```

Output: 
```
{
    "Response": {
        "OrderId": "SO8zRv29",
        "Status": 8,
        "IsAudited": true,
        "RequestId": "9b397ac6-7d01-4fbc-8acc-52dd6ff0877b"
    }
}
```

