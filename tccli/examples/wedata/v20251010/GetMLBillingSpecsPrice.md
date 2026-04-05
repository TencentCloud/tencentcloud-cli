**Example 1: DescribeMLBillingSpecsPrice**



Input: 

```
tccli wedata GetMLBillingSpecsPrice --cli-unfold-argument  \
    --SpecsParam.0.SpecName TI.S.MEDIUM.POST \
    --SpecsParam.0.SpecCount 1
```

Output: 
```
{
    "Response": {
        "Data": {
            "SpecPriceInfos": [
                {
                    "RealTotalCost": 39,
                    "SpecCount": 1,
                    "SpecName": "TI.S.MEDIUM.POST",
                    "TotalCost": 70
                }
            ]
        },
        "RequestId": "297f51dc-bfe0-4a1f-8144-5840de65975d"
    }
}
```

