**Example 1: 查询固件信息**



Input: 

```
tccli iotexplorer DescribeFirmware --cli-unfold-argument  \
    --ProductID I6KTCZ170U \
    --FirmwareVersion t.2
```

Output: 
```
{
    "Response": {
        "Createtime": 1599626765,
        "Description": "固件测试",
        "Md5sum": "1a5c386576074d22a604b795e8917e1a",
        "Name": "固件测试",
        "ProductId": "I6KTCZ170U",
        "ProductName": "8bvsn6go_测试OTA升级",
        "RequestId": "01365e8c-f025-40b9-97a4-fa583d6c569e",
        "Version": "t.2",
        "FwType": "mcu"
    }
}
```

