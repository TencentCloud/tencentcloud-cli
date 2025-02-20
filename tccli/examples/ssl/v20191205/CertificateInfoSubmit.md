**Example 1: 付费证书提交资料 - CFCA品牌证书**

付费证书提交资料

Input: 

```
tccli ssl CertificateInfoSubmit --cli-unfold-argument  \
    --AdminEmail ssl@tencent.com \
    --AdminFirstName 测 \
    --AdminIdNumber 110000000000000001 \
    --AdminIdType SFZ \
    --AdminLastName 试 \
    --AdminPhone 13112341234 \
    --AdminTitle 研发 \
    --CertCommonName tencent.com \
    --CertId J2lX2maH \
    --CompanyId 134 \
    --CompanyType 2 \
    --CsrEncryptAlgo RSA \
    --CsrKeyParameter 2048 \
    --GenCsrType online \
    --ManagerId 2345 \
    --OrgAddress 广东省广州市xx区xxxxxx101号 \
    --OrgCity 广州市 \
    --OrgCountry CN \
    --OrgDivision 研发部 \
    --OrgIdNumber 111111111111110000 \
    --OrgIdType TYDMZ \
    --OrgOrganization 腾讯云SSL证书 \
    --OrgPhoneArea 010 \
    --OrgPhoneNumber 234123123 \
    --OrgRegion 广东省 \
    --TechEmail ssl@tencent.com \
    --TechFirstName 测 \
    --TechIdNumber 110000000000000001 \
    --TechIdType SFZ \
    --TechLastName 试 \
    --TechPhone 13112341234 \
    --TechTitle 研发 \
    --VerifyType FILE
```

Output: 
```
{
    "Response": {
        "RequestId": "54c73858-77a6-435c-addc-65919b550900"
    }
}
```

**Example 2: 付费证书提交资料 - 通用**



Input: 

```
tccli ssl CertificateInfoSubmit --cli-unfold-argument  \
    --CertId LrmeMvQr \
    --GenCsrType online \
    --CertCommonName tencent.com \
    --CompanyType 2 \
    --OrgIdType  \
    --OrgIdNumber  \
    --AdminIdType  \
    --AdminIdNumber  \
    --TechIdType  \
    --TechIdNumber  \
    --CompanyId 11772 \
    --Csr  \
    --KeyPass 12345678 \
    --OrgOrganization 腾讯云SSL证书测试 \
    --OrgDivision 测试部门 \
    --OrgAddress 腾讯云SSL证书测试地址 \
    --OrgCountry CN \
    --OrgCity 北京市 \
    --OrgRegion 北京市 \
    --OrgPhoneArea 010 \
    --OrgPhoneNumber 123456789010 \
    --AdminFirstName 试 \
    --AdminLastName 测 \
    --AdminPhone 18169239105 \
    --AdminEmail ssl@tencent.com \
    --AdminTitle 测试 \
    --TechFirstName 试 \
    --TechLastName 测 \
    --CsrKeyParameter 2048 \
    --CsrEncryptAlgo RSA \
    --TechEmail ssl@tencent.com \
    --TechPhone 18169239105 \
    --TechTitle 测试 \
    --ManagerId 12895
```

Output: 
```
{
    "Response": {
        "RequestId": "54c73858-77a6-435c-addc-65919b550900"
    }
}
```

**Example 3: 付费证书提交资料 - 上传CSR**



Input: 

```
tccli ssl CertificateInfoSubmit --cli-unfold-argument  \
    --CertId LrmeMvQr \
    --GenCsrType parse \
    --CertCommonName tencent.com \
    --CompanyType 2 \
    --OrgIdType  \
    --OrgIdNumber  \
    --AdminIdType  \
    --AdminIdNumber  \
    --TechIdType  \
    --TechIdNumber  \
    --CompanyId 11772 \
    --Csr -----BEGIN CERTIFICATE REQUEST-----
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
    --KeyPass 12345678 \
    --OrgOrganization 腾讯云SSL证书测试 \
    --OrgDivision 测试部门 \
    --OrgAddress 腾讯云SSL证书测试地址 \
    --OrgCountry CN \
    --OrgCity 北京市 \
    --OrgRegion 北京市 \
    --OrgPhoneArea 010 \
    --OrgPhoneNumber 123456789010 \
    --AdminFirstName 试 \
    --AdminLastName 测 \
    --AdminPhone 18162039301 \
    --AdminEmail ssl@tencent.com \
    --AdminTitle 测试 \
    --TechFirstName 试 \
    --TechLastName 测 \
    --CsrKeyParameter  \
    --CsrEncryptAlgo  \
    --TechEmail ssl@tencent.com \
    --TechPhone 18162039301 \
    --TechTitle 测试 \
    --ManagerId 12895
```

Output: 
```
{
    "Response": {
        "RequestId": "54c73858-77a6-435c-addc-65919b550900"
    }
}
```

