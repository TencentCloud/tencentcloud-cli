**Example 1: 用户证书申请**



Input: 

```
tccli tbaas ApplyUserCert --cli-unfold-argument  \
    --Module cert_mng \
    --Operation cert_apply_for_user \
    --ClusterId 251005746bckuobc41mpu \
    --GroupName youtuOrg \
    --UserIdentity kyloz \
    --Applicant 优图SDK \
    --IdentityNum 123 \
    --CsrData -----BEGINCERTIFICATEREQUEST-----
MIIBSTCB8AIBADCBjTELMAkGA1UEBhMCQ04xEjAQBgNVBAgMCUd1YW5nWmhvdTER
MA8GA1UEBwwIU2hlblpoZW4xFDASBgNVBAoMC2V4YW1wbGUuY29tMQ8wDQYDVQQL
DAZjbGllbnQxMDAuBgNVBAMMJ0FkbWluLm9yZzJAb3JnMi5leGFtcGxlLmNvbSx0
eXBlPWNsaWVudDBZMBMGByqGSM49AgEGCCqGSM49AwEHA0IABMIrWeLZjivbTLwy
z+JMfmZjPEJ8x4H8a/CnqBIwcCaJjg5cMqOi+VyFHkCM9Sv4MFOqPAK7rE62m9XF
s4B8hfKgADAKBggqhkjOPQQDAgNIADBFAiEAtl/h0DHfRJl170U6OGpCkN34jX0a
GGGSHbFu2KxLUHsCIAFxXa6UsQOf93vT0FQldeBodbVCbNhM8/jtVqfZ/lhB
-----ENDCERTIFICATEREQUEST----- \
    --Notes test
```

Output: 
```
{
    "Response": {
        "CertDn": "C=CN,ST=ShenZhen,L=4ShenZhen,O=org1,OU=client,CN=kylouse@org1.bcdk3eis17qe@client",
        "CertId": 172634,
        "RequestId": "16824370-6058-4f38-a32d-c19b1eaefaee"
    }
}
```

