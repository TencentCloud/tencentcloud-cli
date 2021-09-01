**Example 1: 提交证书资料**



Input: 

```
tccli ssl SubmitCertificateInformation --cli-unfold-argument  \
    --CertificateId abcb1234 \
    --CsrType online \
    --CertificateDomain *.test-dq342da.com \
    --OrganizationName Tencent \
    --OrganizationDivision Qcloud \
    --OrganizationAddress 南山区腾讯大厦1000号 \
    --OrganizationCountry CN \
    --OrganizationCity 深圳市 \
    --OrganizationRegion 广东省 \
    --PhoneAreaCode 0755 \
    --PhoneNumber 86013388 \
    --AdminFirstName test \
    --AdminLastName test \
    --AdminPhoneNum 12345678901 \
    --AdminEmail test@tencent.com \
    --AdminPosition developer \
    --ContactFirstName test \
    --ContactLastName test \
    --ContactEmail test@tencent.com \
    --ContactNumber 12345678901 \
    --ContactPosition developer
```

Output: 
```
{
    "Response": {
        "CertificateId": "abcb1234",
        "RequestId": "9b397ac6-7d01-4fbc-8acc-52dd6ff0877b"
    }
}
```

