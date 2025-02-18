**Example 1: 示例**

示例

Input: 

```
tccli mqtt RegisterCaCertificate --cli-unfold-argument  \
    --InstanceId mqtt-g4r4x85z \
    --CaCertificate -----BEGIN CERTIFICATE-----
MIIEvDCCA6SgAwIBAgIUGx4783AhEBJYh6OnIafmbwVSJRMwDQYJKoZIhvcNAQEL
-----END CERTIFICATE----- \
    --VerificationCertificate -----BEGIN CERTIFICATE-----
MIID7TCCAtWgAwIBAgIUDu9opYK5QlQpblTOdU+U1welmRIwDQYJKoZIhvcNAQEL
-----END CERTIFICATE-----
```

Output: 
```
{
    "Error": null,
    "RequestId": null,
    "Response": {
        "RequestId": "2773beef-8527-4cc1-9e84-f15d56eaa7d9"
    }
}
```

