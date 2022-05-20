**Example 1: 获取固件列表示例**



Input: 

```
tccli iotcloud ListFirmwares --cli-unfold-argument  \
    --ProductId ABCDE12345 \
    --PageNum 1 \
    --PageSize 10 \
    --Filters.0.Key FirmwareName \
    --Filters.0.Value 123
```

Output: 
```
{
    "Response": {
        "TotalCount": 1,
        "Firmwares": [
            {
                "Version": "1.0.0",
                "Md5sum": "ahbdjshfuisdfoisjfos",
                "CreateTime": "147873872173",
                "Name": "xx",
                "ProductName": "xx",
                "ProductId": "xx",
                "Description": "xx"
            }
        ],
        "RequestId": "xxxxxxxxxxxxxxxxxxxxxxx"
    }
}
```

