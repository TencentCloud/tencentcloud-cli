**Example 1: 导入外部资产信息**



Input: 

```
tccli dasb ImportExternalDevice --cli-unfold-argument  \
    --DeviceSet.0.Ip xx \
    --DeviceSet.0.Name xx \
    --DeviceSet.0.OsName xx \
    --DeviceSet.0.Port 1
```

Output: 
```
{
    "Response": {
        "RequestId": "xx"
    }
}
```

