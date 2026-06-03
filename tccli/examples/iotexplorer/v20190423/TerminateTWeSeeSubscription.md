**Example 1: 退订 TWeSee 视频理解订阅**



Input: 

```
tccli iotexplorer TerminateTWeSeeSubscription --cli-unfold-argument  \
    --ProductId 4AHMY9X89Y \
    --DeviceName dev002 \
    --ServiceType VID_COMP
```

Output: 
```
{
    "Response": {
        "Currency": "CNY",
        "OrderId": "20260420*********539551",
        "Price": "-1160",
        "Status": "DELIVERED",
        "RequestId": "5487cca6-bd04-4a1c-87df-930894b774e0"
    }
}
```

