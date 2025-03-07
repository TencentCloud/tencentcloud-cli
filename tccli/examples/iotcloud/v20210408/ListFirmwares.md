**Example 1:  获取固件列表示例**



Input: 

```
tccli iotcloud ListFirmwares --cli-unfold-argument  \
    --ProductId EQPOKD5111 \
    --PageNum 1 \
    --PageSize 1 \
    --Filters.0.Key dfsg23gfds4 \
    --Filters.0.Value dfeg
```

Output: 
```
{
    "Response": {
        "TotalCount": 1,
        "Firmwares": [
            {
                "Version": "1.0.1",
                "Md5sum": "2f8222b4f275c4f18e69c34f66d2631b",
                "CreateTime": 1,
                "ProductName": "dev-001",
                "Name": "myname",
                "Description": "mydescription",
                "ProductId": "EQPOKD5111",
                "FwType": "mcu",
                "CreateUserId": 1
            }
        ],
        "RequestId": "ebea2fd8-0b8f-44b3-99ab-1b04fcfb6cbc"
    }
}
```

