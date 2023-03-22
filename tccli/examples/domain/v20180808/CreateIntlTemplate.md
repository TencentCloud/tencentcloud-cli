**Example 1: 创建模板**



Input: 

```
tccli domain CreateIntlTemplate --cli-unfold-argument  \
    --RegistrantContact.Province xx \
    --RegistrantContact.City xx \
    --RegistrantContact.Fax xx \
    --RegistrantContact.AddressLine xx \
    --RegistrantContact.FirstName xx \
    --RegistrantContact.CompanyName xx \
    --RegistrantContact.JobTitle xx \
    --RegistrantContact.ZipCode xx \
    --RegistrantContact.AddressLineTwo xx \
    --RegistrantContact.Country xx \
    --RegistrantContact.LastName xx \
    --RegistrantContact.Phone xx \
    --RegistrantContact.Email xx \
    --BillingContact.Province xx \
    --BillingContact.City xx \
    --BillingContact.Fax xx \
    --BillingContact.AddressLine xx \
    --BillingContact.FirstName xx \
    --BillingContact.CompanyName xx \
    --BillingContact.JobTitle xx \
    --BillingContact.ZipCode xx \
    --BillingContact.AddressLineTwo xx \
    --BillingContact.Country xx \
    --BillingContact.LastName xx \
    --BillingContact.Phone xx \
    --BillingContact.Email xx \
    --TechnicalContact.Province xx \
    --TechnicalContact.City xx \
    --TechnicalContact.Fax xx \
    --TechnicalContact.AddressLine xx \
    --TechnicalContact.FirstName xx \
    --TechnicalContact.CompanyName xx \
    --TechnicalContact.JobTitle xx \
    --TechnicalContact.ZipCode xx \
    --TechnicalContact.AddressLineTwo xx \
    --TechnicalContact.Country xx \
    --TechnicalContact.LastName xx \
    --TechnicalContact.Phone xx \
    --TechnicalContact.Email xx \
    --AdminContact.Province xx \
    --AdminContact.City xx \
    --AdminContact.Fax xx \
    --AdminContact.AddressLine xx \
    --AdminContact.FirstName xx \
    --AdminContact.CompanyName xx \
    --AdminContact.JobTitle xx \
    --AdminContact.ZipCode xx \
    --AdminContact.AddressLineTwo xx \
    --AdminContact.Country xx \
    --AdminContact.LastName xx \
    --AdminContact.Phone xx \
    --AdminContact.Email xx
```

Output: 
```
{
    "Response": {
        "RequestId": "xx",
        "TemplateId": "xx"
    }
}
```

