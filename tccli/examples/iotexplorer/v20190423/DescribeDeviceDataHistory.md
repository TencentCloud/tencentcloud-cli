**Example 1: 获取设备历史数据**

获取设备历史数据

Input: 

```
tccli iotexplorer DescribeDeviceDataHistory --cli-unfold-argument  \
    --MinTime 1548677099000 \
    --MaxTime 1548763499000 \
    --ProductId LJ0INDNU7U \
    --DeviceName light1 \
    --FieldName color \
    --Limit 5
```

Output: 
```
{
    "Response": {
        "RequestId": "5c982342-fb08-4fac-8e70-f63834667b52",
        "FieldName": "color",
        "Listover": true,
        "Context": "",
        "Results": [
            {
                "Time": "1550055697000",
                "Value": "1"
            },
            {
                "Time": "1550055698000",
                "Value": "3"
            }
        ]
    }
}
```

