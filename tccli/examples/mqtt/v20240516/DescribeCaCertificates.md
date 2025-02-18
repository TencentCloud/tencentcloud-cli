**Example 1: 示例**

示例

Input: 

```
tccli mqtt DescribeCaCertificates --cli-unfold-argument  \
    --InstanceId mqtt-mmgej724
```

Output: 
```
{
    "Error": null,
    "RequestId": null,
    "Response": {
        "Data": [
            {
                "CaCertificate": "-----BEGIN CERTIFICATE-----\nMIIEvDCCA6SgAwIBAgIUGx4783AhEBJYh6OnIafmbwVSJRMwDQYJKoZIhvcNAQEL\n-----END CERTIFICATE-----",
                "CaCn": "cn",
                "CaSn": "1b1e3bf3702110125887a3a721a7e66f05522513",
                "CreatedTime": 1719992244000,
                "Format": "PEM",
                "Status": "ACTIVE",
                "UpdateTime": 1719992244000,
                "LastInactivationTime": 1719992244000,
                "LastActivationTime": 1719992244000,
                "VerificationCertificate": "-----BEGIN CERTIFICATE-----\nMIID7TCCAtWgAwIBAgIUDu9opYK5QlQpblTOdU+U1welmRIwDQYJKoZIhvcNAQEL\n-----END CERTIFICATE-----"
            }
        ],
        "RequestId": "d03f799b-1244-45d7-9e03-0ceaf8f63fed"
    }
}
```

