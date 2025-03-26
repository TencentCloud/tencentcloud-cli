**Example 1: 获取设备资源列表**



Input: 

```
tccli iotcloud DescribeDeviceResources --cli-unfold-argument  \
    --ProductID EQPOKD5111 \
    --Offset 0 \
    --Limit 10 \
    --DeviceName dev-001 \
    --StartTime '2021-10-21 15:11:11' \
    --EndTime '2021-10-21 18:11:11'
```

Output: 
```
{
    "Response": {
        "TotalCount": 1,
        "Result": [
            {
                "Name": "myname",
                "ProductName": "dev-001",
                "Md5": "418806da363b5b57199e5a9f88fc69c3",
                "DeviceName": "device-001",
                "ProductID": "EQPOKD5111",
                "UpdateTime": "1740563445",
                "Size": 1
            }
        ],
        "RequestId": "5186e731-d43c-43ef-955c-12ff9b0ce9f2"
    }
}
```

