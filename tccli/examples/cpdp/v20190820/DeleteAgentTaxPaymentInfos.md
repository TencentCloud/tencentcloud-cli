**Example 1: DeleteAgentTaxPaymentInfos**



Input: 

```
tccli cpdp DeleteAgentTaxPaymentInfos --cli-unfold-argument  \
    --Placement.Zone ap-guangzhou-2 \
    --ImageId img-pmqg1cw7 \
    --BatchNum 1
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

