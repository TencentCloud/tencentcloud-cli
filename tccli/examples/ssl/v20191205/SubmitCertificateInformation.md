**Example 1: 付费证书提交资料**



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
    --AdminFirstName luke \
    --AdminLastName sky \
    --AdminPhoneNum 12345678901 \
    --AdminEmail test@tencent.com \
    --AdminPosition developer \
    --ContactFirstName luke \
    --ContactLastName sky \
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

**Example 2: 付费证书提交资料 - 上传CSR**



Input: 

```
tccli ssl SubmitCertificateInformation --cli-unfold-argument  \
    --CertificateId LrmeMvQr \
    --CsrType parse \
    --CsrContent -----BEGIN CERTIFICATE REQUEST-----
MIIC5zCCAc8CAQAweTELMAkGA1UEBhMCQ04xEjAQBgNVBAgMCea5luWNl+ecgTES
MBAGA1UEBwwJ6ZW/5rKZ5biCMRswGQYDVQQKDBLohb7orq/kupFTU0zor4HkuaYx
DzANBgNVBAsMBueglOWPkTEUMBIGA1UEAxMLdGVuY2VudC5jb20wggEiMA0GCSqG
SIb3DQEBAQUAA4IBDwAwggEKAoIBAQDWACnWh6gA1dGDi/pJtGZtp/Wp4ou6//JM
Eu4OpXQ5t/afvX4xPGm7laWE4aFItZpfhXc1SGVwOBwWsOArw9xwmdCDFY3Icbu9
8O1mIAIYfMDuc8bWL5lQfuyBeGJw+9i++E/1SkYnx3sRD+vMNlJdkaueWW4qXVo+
ZnE7FX/6Mqi1PE53ccXU55iviLHAaSnztpmUmF4vcKIVbDTsI2TF1raHwdnmvQFx
vifh7h49xRz3Jj3QWCJqdtGKAktFzofDCYPKcIKT4A52u7WsoBspLIds1H93dITD
VxnZaE3oe4sHfQpnlHRbO72Cz1QEgGBQeOW/wH8/WygFiRIWHwZpAgMBAAGgKTAn
BgkqhkiG9w0BCQ4xGjAYMBYGA1UdEQQPMA2CC3RlbmNlbnQuY29tMA0GCSqGSIb3
DQEBCwUAA4IBAQAcr+Wy3uqr+PL+uUMwd1scB7x27/j2JDXTKBdZnsLnaEFCzz2f
y4aqN7hWLHNEoqGGNSg5luKO6DCFXOnzu6/bI4Ziy/w003RD1wMPinpo0C0YIzwM
W99sDPoI1qIxAoNEVLOP11EnPPdlq/D7T4UOMjPxjYSo4Ge2BcG5Bk1zTu/O8She
xHc6lEWniExaYomIboULnLTdSI1Dx0g7segNMvhLGUjRyump3/0jANfk7qbS0Nnz
6Q/i0NmiqUiA38iTdIBY57QAJBbXiJJ3HRF5wZyJESobTr9dHPuZH4ebJvfSaNBp
4KqzUxjAe5GZJs/z5EuJkG/LC/h1L3rFT7AS
-----END CERTIFICATE REQUEST-----
 \
    --CertificateDomain tencent.com \
    --OrganizationName 腾讯云SSL证书测试 \
    --OrganizationDivision Qcloud \
    --OrganizationAddress 南山区腾讯大厦1000号 \
    --OrganizationCountry CN \
    --OrganizationCity 深圳市 \
    --OrganizationRegion 广东省 \
    --PhoneAreaCode 0755 \
    --PhoneNumber 86013388 \
    --AdminFirstName luke \
    --AdminLastName sky \
    --AdminPhoneNum 12345678901 \
    --AdminEmail test@tencent.com \
    --AdminPosition developer \
    --ContactFirstName luke \
    --ContactLastName sky \
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

