**Example 1: 示例**

示例

Input: 

```
tccli mqtt DescribeDeviceCertificate --cli-unfold-argument  \
    --DeviceCertificateSn 0eef68a582b94254296e54ce754f94d707a59911 \
    --InstanceId mqtt-jbgwp4ae
```

Output: 
```
{
    "Error": null,
    "RequestId": null,
    "Response": {
        "CaSn": "1b1e3bf3702110125887a3a721a7e66f05522513",
        "CertificateSource": "API",
        "ClientId": "111",
        "CreatedTime": 1724050379000,
        "DeviceCertificate": "-----BEGIN CERTIFICATE-----\nMIIEQjCCAyqgAwIBAgIUDu9opYK5QlQpblTOdU+U1welmREwDQYJKoZIhvcNAQEL\n-----END CERTIFICATE-----\n",
        "DeviceCertificateCn": "mqtt-test.xxx.tencent.com",
        "DeviceCertificateSn": "0eef68a582b94254296e54ce754f94d707a59911",
        "Format": "PEM",
        "LastActivationTime": 1724050378987,
        "LastInactivationTime": 0,
        "NotAfterTime": 1758185683000,
        "NotBeforeTime": 1714985683000,
        "RequestId": "1b5fc3fa-4bbf-421a-aad1-c45d49119a2c",
        "Status": "ACTIVE",
        "UpdateTime": 1724050379000
    }
}
```

