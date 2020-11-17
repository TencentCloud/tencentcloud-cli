**Example 1: GetSmsAmountInfo**



Input: 

```
tccli zj GetSmsAmountInfo --cli-unfold-argument  \
    --License xxx
```

Output: 
```
{
    "Response": {
        "Data": {
            "SmsCampaignAmount": 123,
            "SmsCampaignConsume": 123,
            "SmsSendAmount": 123,
            "SmsSendConsume": 123,
            "MmsCampaignAmount": 123,
            "MmsCampaignConsume": 123,
            "MmsSendAmount": 123,
            "MmsSendConsume": 123
        },
        "RequestId": "xxx"
    }
}
```

