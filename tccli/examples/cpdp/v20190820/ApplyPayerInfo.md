**Example 1: ApplyPayerInfo**



Input: 

```
tccli cpdp ApplyPayerInfo --cli-unfold-argument  \
    --PayerId qyfkr201911230006 \
    --PayerType CORPORATE \
    --PayerName 企业名称 \
    --PayerIdType UNIFIED_CREDIT_CODE \
    --PayerIdNo 913302127996560011 \
    --PayerCountryCode CHN
```

Output: 
```
{
    "Response": {
        "RequestId": "7cdcbb01-127e-4285-9aca-aa77ca55f028",
        "Result": {
            "Data": {
                "Status": "PAYER_INFO_APPROVED",
                "PayerId": "qyfkr201911230006",
                "MerchantId": "202002270000054004",
                "FailReason": null
            },
            "Code": "000000"
        }
    }
}
```

