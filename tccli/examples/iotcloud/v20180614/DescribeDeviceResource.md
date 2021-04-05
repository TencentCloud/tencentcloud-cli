**Example 1: 查询设备资源详情**



Input: 

```
tccli iotcloud DescribeDeviceResource --cli-unfold-argument  \
    --ProductID ABCDE12345 \
    --Name test \
    --DeviceName test
```

Output: 
```
{
    "Response": {
        "Result": {
            "Status": 1,
            "DeviceName": "xx",
            "UpdateTime": "xx",
            "Name": "xx",
            "Percent": 1,
            "ProductName": "xx",
            "Md5": "xx",
            "ProductID": "xx",
            "Size": 1
        },
        "RequestId": "xx"
    }
}
```

