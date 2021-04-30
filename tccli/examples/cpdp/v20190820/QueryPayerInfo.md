**Example 1: QueryPayerInfo**



Input: 

```
tccli cpdp QueryPayerInfo --cli-unfold-argument  \
    --PayerId qyfkr201911230006
```

Output: 
```
{
    "Response": {
        "RequestId": "8c6ffdae-3a65-4808-9d94-874fc1f9e962",
        "Result": {
            "Data": {
                "Status": "PAYER_INFO_APPROVED",
                "PayerId": "qyfkr201911230006",
                "PayerType": "CORPORATE",
                "PayerContactName": "张三",
                "FailReason": null,
                "MerchantId": "202002270000054004",
                "PayerName": "企业名称B",
                "PayerEmailAddress": null,
                "PayerIdType": "UNIFIED_CREDIT_CODE",
                "PayerCountryCode": "CHN",
                "PayerIdNo": "913302127996560011",
                "PayerContactNumber": "1999999999"
            },
            "Code": "000000"
        }
    }
}
```

