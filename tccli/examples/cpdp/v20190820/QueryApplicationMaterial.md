**Example 1: QueryApplicationMaterial**



Input: 

```
tccli cpdp QueryApplicationMaterial --cli-unfold-argument  \
    --DeclareId dcldid201911230011
```

Output: 
```
{
    "Response": {
        "RequestId": "66ff21b9-caad-466b-9173-c9ec8c99ca61",
        "Result": {
            "Data": {
                "Status": null,
                "DeclareId": "dcldid201911230011",
                "OriginalDeclareId": null,
                "PayerId": "qyfkr201911230004",
                "SourceCurrency": "CNY",
                "SourceAmount": "10.00",
                "MerchantId": "202002270000054004",
                "TradeCode": "223010",
                "TargetAmount": null,
                "TargetCurrency": "USD",
                "TransactionId": "trasid201911230011"
            },
            "Code": "000000"
        }
    }
}
```

