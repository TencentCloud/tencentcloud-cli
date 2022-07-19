**Example 1: 获取固件列表**



Input: 

```
tccli iotvideo ListFirmwares --cli-unfold-argument  \
    --ProductID ABCDE12345 \
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
                "Name": "xx",
                "ProductName": "xx",
                "ProductId": "xx",
                "Description": "xx",
                "Version": "1.0.0",
                "Md5sum": "ahbdjshfuisdfoisjfos",
                "CreateTime": "147873872173"
            }
        ],
        "RequestId": "xxxxxxxxxxxxxxxxxxxxxxx"
    }
}
```

