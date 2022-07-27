**Example 1: 企业认证接口**



Input: 

```
tccli bma CreateCRCompanyVerify --cli-unfold-argument  \
    --CompanyName xxx \
    --CompanyID xxx \
    --CompanyLegalName xxx \
    --ManagerName xxx \
    --ManagerPhone xxx \
    --VerificationCode xxx \
    --CompanyIDType 1
```

Output: 
```
{
    "Response": {
        "Status": 0,
        "Note": "xxx",
        "RequestId": "xxx"
    }
}
```

