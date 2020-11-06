**Example 1: 查询固件信息**



Input: 

```
tccli iotcloud DescribeFirmware --cli-unfold-argument  \
    --ProductID 7ZISKXPJVU \
    --FirmwareVersion 1.0.3 \
    --Md5sum xxxxxxxxxx \
    --FileSize 1024
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
        "ProductName": "ABC"
    }
}
```

