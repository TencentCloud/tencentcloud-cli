**Example 1: 示例**

获取固件列表

Input: 

```
tccli iotexplorer ListFirmwares --cli-unfold-argument  \
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
                "Name": "name",
                "Description": "",
                "FwType": "mcu",
                "CreateUserId": 100028519429,
                "Md5sum": "1***26",
                "ProductName": "name",
                "Version": "v1.0.1.0",
                "ProductId": "Q10***NE",
                "CreateTime": 1678096213,
                "CreatorNickName": "name"
            }
        ],
        "RequestId": "5dcc485f-0c1c-429d-91b0-1534e10dce98"
    }
}
```

