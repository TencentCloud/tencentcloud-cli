**Example 1: 示例**

示例

Input: 

```
tccli mqtt RegisterCaCertificate --cli-unfold-argument  \
    --InstanceId mqtt-g839agr2 \
    --CaCertificate -----BEGIN CERTIFICATE-----
MIIDYDCCAkigAwIBAgIRAJVqMNqSe05LAgWS1VrHft3KJdndK4HflxgRqnmyUfSCRz6R0wXFi4I7no7BfwQahq9Z4IWaHh/6iDoZ1c+
pEkIucoi48CxEbAan8f0a4K4X6jcotXW7FPzZBTZw+swW3H3NvaHrT1shm0W2B7Q
/G2ncyYw6OPFxhBKIfhbgfH7PughdsT7+QsuFYpbs4V6Wydb1NuloFpIeJgSnoQX
GWOLN7DU9WaJCLXon0AejXTgSop/O4He9W00yQFzn7TiPMLV91i6s4qD9/Iin/Wt
AV3BoRcAAn1ryJQS4T5eRqWEy7swndP28HcdNYUZc9mIcqEmqPSejL6Oi9AlnYuX
kRQnRQ==
-----END CERTIFICATE----- \
    --VerificationCertificate -----BEGIN CERTIFICATE-----
MIIDhDCCAmygAwIBAgIRAICF9S7OW9iDCN9tmNlwdxYwDQYJKoZIhvcNAQELBQAw
PzELMAkGA1UEBhMCQ04xGzAZBgNVBAoTEkCWzSiQtf84fwVXUqCOgfd9RHYZQx+bSBEKzt2Nxb15xNMXFzYEm8S0
lQUacxx1N7w/fOed16c+VPMvwhLJSkO7oCbUl8X+hZDY6D326A6muaW0KsBTld4p
ociDefD8oNH+u4qCrcoAPNuhbG44dcqOrrHFlX0offDYjPLAoIgTb8Q/DwhuLg1b
Quw/YMVFLMrMO2wzbu12PzEYmbohbk6Cv0viRFsxd/HUWPNYxi6HnoqpCKBnDwlZ
c/GuUTJ7tFmkb4bKNK81rViXHt3x2fVG6yJwrVw6m3KjhrOKro82AA==
-----END CERTIFICATE-----
```

Output: 
```
{
    "Error": null,
    "RequestId": null,
    "Response": {
        "CaSn": "956a30da927b4e4b020592d55ad7bc7c",
        "InstanceId": "mqtt-g839agr2",
        "RequestId": "8018b411-8963-4c50-81de-c371cb9b0796"
    }
}
```

