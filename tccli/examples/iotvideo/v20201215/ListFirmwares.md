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
                "Name": "bane",
                "ProductName": "product",
                "ProductId": "id",
                "Description": "desc",
                "Version": "1.0.0",
                "Md5sum": "ahbdjshfuisdfoisjfos",
                "CreateTime": "147873872173"
            }
        ],
        "RequestId": "id"
    }
}
```

