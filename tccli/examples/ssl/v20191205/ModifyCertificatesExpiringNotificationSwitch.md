**Example 1: 修改是否忽略证书到期通知**

修改是否忽略证书到期通知

Input: 

```
tccli ssl ModifyCertificatesExpiringNotificationSwitch --cli-unfold-argument  \
    --SwitchStatus 1 \
    --CertificateIds xx
```

Output: 
```
{
    "Response": {
        "RequestId": "xx",
        "CertificateIds": [
            "xx"
        ]
    }
}
```

