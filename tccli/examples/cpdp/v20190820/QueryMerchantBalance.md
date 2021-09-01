**Example 1: QueryMerchantBalance**



Input: 

```
tccli cpdp QueryMerchantBalance --cli-unfold-argument  \
    --Currency CNY
```

Output: 
```
{
    "Response": {
        "RequestId": "817434e7-050e-4a94-b649-63dcb61d3464",
        "Result": {
            "Data": {
                "Currency": "CNY",
                "MerchantId": "202002270000054004",
                "Balance": "1000000.00"
            },
            "Code": "000000"
        }
    }
}
```

