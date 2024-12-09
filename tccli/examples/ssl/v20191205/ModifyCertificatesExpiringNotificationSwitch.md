**Example 1: 修改是否忽略证书到期通知**

修改是否忽略证书到期通知

Input: 

```
tccli ssl ModifyCertificatesExpiringNotificationSwitch --cli-unfold-argument  \
    --SwitchStatus 1 \
    --CertificateIds Thd**jjd
```

Output: 
```
{
    "Response": {
        "RequestId": "14727a68-3b90-4408-99c9-dea6d7de9456",
        "CertificateIds": [
            "Thd**jjd"
        ]
    }
}
```

