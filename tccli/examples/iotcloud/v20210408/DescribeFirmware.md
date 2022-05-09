**Example 1: 查询固件信息**



Input: 

```
tccli iotcloud DescribeFirmware --cli-unfold-argument  \
    --ProductId 7ZISKXPJVU \
    --FirmwareVersion 1.0.3
```

Output: 
```
{
    "Response": {
        "Description": "desc",
        "Md5sum": "md5",
        "FwType": "mcu",
        "Createtime": 1597047368,
        "RequestId": "xxxxxxxxxx",
        "Version": "1.0.3",
        "ProductId": "7ZISKXPJVU",
        "Name": "name",
        "ProductName": "ABC"
    }
}
```

