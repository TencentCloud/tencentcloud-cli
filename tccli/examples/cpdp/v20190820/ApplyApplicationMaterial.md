**Example 1: ApplyApplicationMaterial**



Input: 

```
tccli cpdp ApplyApplicationMaterial --cli-unfold-argument  \
    --TransactionId trasid201911230012 \
    --DeclareId dcldid201911230012 \
    --PayerId qyfkr201911230004 \
    --SourceCurrency CNY \
    --TargetCurrency CNY \
    --TradeCode 223010
```

Output: 
```
{
    "Response": {
        "RequestId": "58529016-114c-43a8-ba51-8b5f290e22be",
        "Result": {
            "Data": {
                "Status": "DECLARE_SUCCESS",
                "OriginalDeclareId": null,
                "DeclareId": "dcldid201911230012",
                "PayerId": "qyfkr201911230004",
                "MerchantId": "202002270000054004",
                "TransactionId": "trasid201911230012"
            },
            "Code": "000000"
        }
    }
}
```

