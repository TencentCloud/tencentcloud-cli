**Example 1: DidCreateTrend**

DID注册量趋势接口

Input: 

```
tccli tdid GetDidRegisterTrend --cli-unfold-argument  \
    --EndTime xx \
    --ClusterId xx \
    --StartTime xx
```

Output: 
```
{
    "Response": {
        "Trend": [
            {
                "Time": "2021-04-23",
                "Count": 50
            },
            {
                "Time": "2021-04-24",
                "Count": 20
            }
        ],
        "RequestId": "eac6b301-a322-493a-8e36-83b295459397"
    }
}
```

