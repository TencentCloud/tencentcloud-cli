**Example 1: 查询设备资源详情**



Input: 

```
tccli iotcloud DescribeDeviceResource --cli-unfold-argument  \
    --ProductID EQPOKD5111 \
    --Name myname \
    --DeviceName dev-001
```

Output: 
```
{
    "Response": {
        "Result": {
            "Status": 1,
            "DeviceName": "myname",
            "UpdateTime": "1740563445",
            "Name": "myname",
            "Percent": 1,
            "ProductName": "dev-001",
            "Md5": "b59c67bf196a4758191e42f76670ceba",
            "ProductID": "EQPOKD5111",
            "Size": 1
        },
        "RequestId": "5186e731-d43c-43ef-955c-12ff9b0ce9f9"
    }
}
```

