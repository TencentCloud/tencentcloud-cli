**Example 1: 示例**

示例

Input: 

```
tccli mqtt DescribeCaCertificate --cli-unfold-argument  \
    --CaSn 1b1e3bf3702110125887a3a721a7e66f05522513 \
    --InstanceId mqtt-jbgwp4ae
```

Output: 
```
{
    "Error": null,
    "RequestId": null,
    "Response": {
        "CaCertificate": "-----BEGIN CERTIFICATE-----\nMIIEvDCCA6SgAwIBAgIUGx4783AhEBJYh6OnIafmbwVSJRMwDQYJKoZIhvcNAQEL\nBQAwgZIxCzAJBgNVBAYTAmNuMQ0wCwYDVQQIDAR4aWFuMQ0wCwYDVQQHDARodXlp\nMREwDwYDVQQKDAhqZWhhbnN1bjEWMBQGA1UECwwNdW5pdCBqZWhhbnN1bjEVMBMG\nA1UEAwwMc3Vuamlhbnhpb25nMSMwIQYJKoZIhvc1UEBwwEaHV5aTERMA8GA1UECgwI\namVoYW5zdW4xFjAUBgNVB\n-----END CERTIFICATE-----\n",
        "CaCn": "ca.cloud.tencent.com",
        "CaIssuerCn": "a.cloud.tencent.com",
        "CaSn": "1b1e3bf3702110125887a3a721a7e66f05522513",
        "CreatedTime": 1724050364000,
        "Format": "PEM",
        "LastActivationTime": 1724050364340,
        "LastInactivationTime": 0,
        "NotAfterTime": 2030344601000,
        "NotBeforeTime": 1724052316000,
        "RequestId": "7cb5d884-35a0-4f35-9cca-24c7d748a034",
        "Status": "ACTIVE",
        "UpdateTime": 1724050364000
    }
}
```

