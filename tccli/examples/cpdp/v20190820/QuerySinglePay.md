**Example 1: QuerySinglePay**



Input: 

```
tccli cpdp QuerySinglePay --cli-unfold-argument  \
    --Placement.Zone ap-guangzhou-2 \
    --SerialNumber 123123123
```

Output: 
```
{
    "Response": {
        "RequestId": "9b919ced-362c-4190-8cb8-cc6216526bfb",
        "Result": {
            "SerialNo": "123123123",
            "HandleStatus": "S",
            "Items": [
                {
                    "PayStatus": "P",
                    "PlatformMsg": null,
                    "BankRetMsg": null,
                    "BankRetCode": null
                }
            ],
            "HandleMsg": null
        }
    }
}
```

