**Example 1: 查询固件信息**



Input: 

```
tccli iotvideo DescribeFirmware --cli-unfold-argument  \
    --ProductID 7ZISKXPJVU \
    --FirmwareVersion 1.0.3
```

Output: 
```
{
    "Response": {
        "Description": "desc",
        "Md5sum": "md5",
        "Createtime": 1597047368,
        "RequestId": "xxxxxxxxxx",
        "Version": "1.0.3",
        "ProductId": "7ZISKXPJVU",
        "Name": "name",
        "ProductName": "ABC",
        "FwType": "mcu"
    }
}
```

