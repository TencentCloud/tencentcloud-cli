**Example 1: 示例**

示例

Input: 

```
tccli mqtt RegisterDeviceCertificate --cli-unfold-argument  \
    --InstanceId mqtt-g839agr2 \
    --DeviceCertificate -----BEGIN CERTIFICATE-----
MIIDhDCCAmygAwIBAgIRAICF9S7OW9iDCN9tmNlwdxYwDQYJKoZIhvcNAQEFAAOCAQEAJ5a40Jc63eGlrz6M92YpiodMA8C8RMo2
eWfUCxMPSHCWzSiQtf84fwVXUqCOgfd9RHYZQx+bSBEKzt2Nxb15xNMXFzYEm8S0
lQUacxx1N7w/fOed16c+VPMvwhLJSkO7oCbUl8X+hZDY6D326A6muaW0KsBTld4p
ociDefD8oNH+u4qCrcoAPNuhbG44dcqOrrHFlX0offDYjPLAoIgTb8Q/DwhuLg1b
Quw/YMVFLMrMO2wzbu12PzEYmbohbk6Cv0viRFsxd/HUWPNYxi6HnoqpCKBnDwlZ
c/GuUTJ7tFmkb4bKNK81rViXHt3x2fVG6yJwrVw6m3KjhrOKro82AA==
-----END CERTIFICATE----- \
    --CaSn 956a30da927b4e4b020592d55ad7bc7c
```

Output: 
```
{
    "Error": null,
    "RequestId": null,
    "Response": {
        "CaSn": "956a30da927b4e4b020592d55ad7bc7c",
        "DeviceCertificateSn": "8085f52ece5bd88308df6d98d9707716",
        "InstanceId": "mqtt-g839agr2",
        "RequestId": "05e8b3d9-9cee-478f-9d68-b70fda94c61f"
    }
}
```

