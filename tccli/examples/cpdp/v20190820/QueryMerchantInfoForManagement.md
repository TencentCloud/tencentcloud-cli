**Example 1: QueryMerchantInfoForManagement**



Input: 

```
tccli cpdp QueryMerchantInfoForManagement --cli-unfold-argument  \
    --Placement.Zone ap-guangzhou-2\
    --ImageId img-pmqg1cw7\
    --InvoicePlatformId 0\
    --Offset 0\
    --Limit 10
```

Output: 
```
{
    "Response": {
        "RequestId": "CPDP-1585143238239",
        "Result": {
            "Total": 1,
            "List": [
                {
                    "Invoiceplatformid": 0,
                    "Serialno": "CPDP-a55958912dde",
                    "Taxregistrationcertificate": " ",
                    "Email": "",
                    "Address": "",
                    "Message": "工单审核通过,已完成",
                    "Updatetime": 1585012074000,
                    "Authorizationcode": "",
                    "Appid": "test",
                    "Createtime": 1585012074000,
                    "Phone": "",
                    "Expressno": "",
                    "Platformcode": "",
                    "Legalpersonname": "",
                    "Drawer": "drawer",
                    "Code": "0",
                    "Reviewer": "reviewer",
                    "Taxpayernum": "",
                    "Callbackurl": "",
                    "Bankname": "",
                    "Taxpayername": "",
                    "Bankaccount": "",
                    "Contactsname": "",
                    "Regioncode": 44,
                    "State": "1",
                    "Registrationcode": "",
                    "Expressname": "",
                    "Cityname": "",
                    "Payee": ""
                }
            ]
        }
    }
}
```

