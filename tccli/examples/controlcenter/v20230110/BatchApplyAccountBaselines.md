**Example 1: 批量对存量账号应用基线**

批量对存量账号应用基线

Input: 

```
tccli controlcenter BatchApplyAccountBaselines --cli-unfold-argument  \
    --MemberUinList 13436673356 \
    --BaselineConfigItems.0.Identifier ACS-BP_ACCOUNT_FACTORY_ACCOUNT_CONTACT \
    --BaselineConfigItems.0.Configuration {"Contacts":[{"Name":"dest","Email":"ia@22.com","Mobile":"12345678910","Position":"Technical Director"}]}
```

Output: 
```
{
    "Response": {
        "RequestId": "e2f35fb3-3c8c-431e-b318-b4746cfe076c"
    }
}
```

