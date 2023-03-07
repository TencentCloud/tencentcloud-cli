**Example 1: 查询客户信用额度**



Input: 

```
tccli intlpartnersmgt QueryCustomersCredit --cli-unfold-argument ```

Output: 
```
{
    "Response": {
        "Total": 1,
        "Data": [
            {
                "ClientUin": 1,
                "Name": "abcdefg@tencent.com",
                "Mobile": "131123456789",
                "RecentExpiry": "2022-10-13 20:09:03",
                "RemainingCredit": 100,
                "Remark": "remark",
                "Credit": 100,
                "AssociationTime": "2022-10-13 20:09:03",
                "IdentifyType": 1,
                "Type": "new",
                "Email": "abcd*********@tencent.com",
                "Arrears": "-"
            }
        ],
        "RequestId": "2b7c676e-bb4b-449d-89e6-4866132036c4"
    }
}
```

