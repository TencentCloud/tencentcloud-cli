**Example 1: 计算中心-计算税前金额**



Input: 

```
tccli cpdp QueryFlexAmountBeforeTax --cli-unfold-argument  \
    --AmountAfterTax 800 \
    --IncomeType OCCASION \
    --PayeeId 1524013479128928256
```

Output: 
```
{
    "Response": {
        "ErrCode": "0",
        "ErrMessage": "success",
        "Result": {
            "AmountBeforeTax": "1000.000000"
        },
        "RequestId": "08ce6fb8-9321-4d7e-be49-2a95dd8ebebc"
    }
}
```

