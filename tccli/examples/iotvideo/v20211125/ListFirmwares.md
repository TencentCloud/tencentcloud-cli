**Example 1: 获取固件列表**



Input: 

```
tccli iotvideo ListFirmwares --cli-unfold-argument  \
    --ProductID product \
    --PageNum 1 \
    --PageSize 10
```

Output: 
```
{
    "Response": {
        "TotalCount": 1,
        "Firmwares": [
            {
                "Name": "firm",
                "ProductName": "UWUJ98XC0",
                "ProductId": "UWUJ98XC0",
                "Description": "desc",
                "Version": "1.0.0",
                "Md5sum": "ahbdjshfuisdfoisjfos",
                "CreateTime": "147873872173",
                "FwType": "mcu"
            }
        ],
        "RequestId": "id"
    }
}
```

