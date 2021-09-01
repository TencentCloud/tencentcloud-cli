**Example 1: QueryExchangeRate**



Input: 

```
tccli cpdp QueryExchangeRate --cli-unfold-argument  \
    --SourceCurrency CNY \
    --TargetCurrency USD
```

Output: 
```
{
    "Response": {
        "RequestId": "2993188e-6ea2-4e27-b9ab-8adcd21a259d",
        "Result": {
            "Data": [
                {
                    "SourceCurrency": "CNY",
                    "Rate": "6.85220000",
                    "BaseCurrency": "USD",
                    "RateTime": "2020-04-13 09:45:00",
                    "TargetCurrency": "USD"
                }
            ],
            "Code": "000000"
        }
    }
}
```

