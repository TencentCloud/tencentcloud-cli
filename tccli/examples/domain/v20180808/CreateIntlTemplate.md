**Example 1: 创建模板**



Input: 

```
tccli domain CreateIntlTemplate --cli-unfold-argument  \
    --AdminContact.AddressLine ***, HongKong \
    --AdminContact.City Hong Kong \
    --AdminContact.CompanyName HONG KONG *** \
    --AdminContact.Country HK \
    --AdminContact.Email l***5@gmail.com \
    --AdminContact.FirstName *GY \
    --AdminContact.LastName *U \
    --AdminContact.Phone +86.1** \
    --AdminContact.Province Hong Kong \
    --AdminContact.ZipCode **7 \
    --BillingContact.AddressLine ***, HongKong \
    --BillingContact.City Hong Kong \
    --BillingContact.CompanyName HONG KONG *** \
    --BillingContact.Country HK \
    --BillingContact.Email l***5@gmail.com \
    --BillingContact.FirstName *GY \
    --BillingContact.LastName *U \
    --BillingContact.Phone +86.1** \
    --BillingContact.Province Hong Kong \
    --BillingContact.ZipCode **7 \
    --RegistrantContact.AddressLine ***, HongKong \
    --RegistrantContact.City Hong Kong \
    --RegistrantContact.CompanyName HONG KONG *** \
    --RegistrantContact.Country HK \
    --RegistrantContact.Email l***5@gmail.com \
    --RegistrantContact.FirstName *GY \
    --RegistrantContact.LastName *U \
    --RegistrantContact.Phone +86.1** \
    --RegistrantContact.Province Hong Kong \
    --RegistrantContact.ZipCode **7 \
    --TechnicalContact.AddressLine ***, HongKong \
    --TechnicalContact.City Hong Kong \
    --TechnicalContact.CompanyName HONG KONG *** \
    --TechnicalContact.Country HK \
    --TechnicalContact.Email l***5@gmail.com \
    --TechnicalContact.FirstName *GY \
    --TechnicalContact.LastName *U \
    --TechnicalContact.Phone +86.1** \
    --TechnicalContact.Province Hong Kong \
    --TechnicalContact.ZipCode **7 \
    --TemplateType E
```

Output: 
```
{
    "Response": {
        "TemplateId": "temp-2349derf",
        "RequestId": "dwert-eeewr-fsdwe-fwert"
    }
}
```

