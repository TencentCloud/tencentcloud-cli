**Example 1: 付费证书提交资料**

付费证书提交资料

Input: 

```
tccli ssl CertificateInfoSubmit --cli-unfold-argument  \
    --CertId abc \
    --GenCsrType abc \
    --Csr abc \
    --CertCommonName abc \
    --DnsNames abc \
    --KeyPass abc \
    --OrgOrganization abc \
    --OrgDivision abc \
    --OrgAddress abc \
    --OrgCountry abc \
    --OrgCity abc \
    --OrgRegion abc \
    --OrgPhoneArea abc \
    --OrgPhoneNumber abc \
    --VerifyType abc \
    --AdminFirstName abc \
    --AdminLastName abc \
    --AdminPhone abc \
    --AdminEmail abc \
    --AdminTitle abc \
    --TechFirstName abc \
    --TechLastName abc \
    --ContactEmail abc \
    --CompanyType 1 \
    --AutoRenewFlag 1 \
    --CsrKeyParameter abc \
    --CsrEncryptAlgo abc \
    --ManagerId abc \
    --TechPhone abc \
    --TechEmail abc \
    --TechTitle abc \
    --OrgIdType abc \
    --OrgIdNumber abc \
    --AdminIdType abc \
    --AdminIdNumber abc \
    --TechIdType abc \
    --TechIdNumber abc \
    --CompanyId abc
```

Output: 
```
{
    "Response": {
        "RequestId": "abc"
    }
}
```

