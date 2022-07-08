**Example 1: 获取设备属性数据**



Input: 

```
tccli iotvideo DescribeDeviceData --cli-unfold-argument  \
    --ProductId 8JEJGX22EY \
    --DeviceName T0_73043894_1
```

Output: 
```
{
    "Response": {
        "RequestId": "ac74ecca-b866-4ab1-87e0-18b92816fb20",
        "Data": "{\"_sys_cs_days\":{\"Value\":3,\"LastUpdate\":1650867145047},\"_sys_cs_status\":{\"Value\":1,\"LastUpdate\":1650867145047},\"_sys_cs_type\":{\"Value\":2,\"LastUpdate\":1650867145047}}"
    }
}
```

