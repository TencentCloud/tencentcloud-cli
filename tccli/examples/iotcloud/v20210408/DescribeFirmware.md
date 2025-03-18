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
        "Description": "mydescription",
        "Md5sum": "418806da363b5b57199e5a9f88fc69c3",
        "FwType": "mcu",
        "Createtime": 1597047368,
        "RequestId": "5186e731-d43c-43ef-955c-12ff9b0ce9f2",
        "Version": "1.0.3",
        "ProductId": "7ZISKXPJVU",
        "Name": "myname",
        "ProductName": "dev-001"
    }
}
```

