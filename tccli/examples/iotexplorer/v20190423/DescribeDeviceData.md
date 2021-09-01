**Example 1: 获取设备数据**

获取设备数据

Input: 

```
tccli iotexplorer DescribeDeviceData --cli-unfold-argument  \
    --ProductId LJ0INDNU7U \
    --DeviceName light1
```

Output: 
```
{
    "Response": {
        "Data": "{\"brightness\":{\"Value\":5,\"LastUpdate\":1551432955984},\"color\":{\"Value\":11,\"LastUpdate\":1551432955984},\"name\":{\"Value\":\"light of city\",\"LastUpdate\":1551432955984}}",
        "RequestId": "5c982342-fb08-4fac-8e70-f63834667b52"
    }
}
```

