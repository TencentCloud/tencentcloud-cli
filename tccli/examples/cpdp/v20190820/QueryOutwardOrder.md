**Example 1: QueryOutwardOrder**



Input: 

```
tccli cpdp QueryOutwardOrder --cli-unfold-argument  \
    --TransactionId trasid201911230012
```

Output: 
```
{
    "Response": {
        "RequestId": "95965399-d7ef-42b4-acb5-516498554a5f",
        "Result": {
            "Data": {
                "FxRate": null,
                "PricingCurrency": "CNY",
                "FailReason": null,
                "MerchantId": "202002270000054004",
                "TargetCurrency": "USD",
                "TargetAmount": null,
                "Status": "WAIT_PAYMENT",
                "SourceCurrency": "CNY",
                "SourceAmount": "10.00",
                "AcctDate": null,
                "RefundAmount": null,
                "TransactionId": "trasid201911230012",
                "RefundCurrency": null
            },
            "Code": "000000"
        }
    }
}
```

