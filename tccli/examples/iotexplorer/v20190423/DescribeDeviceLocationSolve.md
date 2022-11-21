**Example 1: 获取实时位置解析**

获取实时位置解析

Input: 

```
tccli iotexplorer DescribeDeviceLocationSolve --cli-unfold-argument  \
    --LocationType GNSSNavigation \
    --DeviceName  \
    --ProductId  \
    --GNSSNavigation {"captures":[{"payload":"82d3ef004114d419ecf7ef4ed40bbf4ab588f1a419b56a275264a6b8cd01"},{"payload":"82d3ef004114331ad480d459ab49d4787e67fdd2760bdb65e70c"}]}
```

Output: 
```
{
    "Response": {
        "Longitude": 113.93931,
        "Latitude": 22.54099,
        "LocationType": "GNSSNavigation",
        "Accuracy": 54.5,
        "RequestId": "1e99faaf-a0f0-4c49-9d85-7f09f2b7f74e"
    }
}
```

