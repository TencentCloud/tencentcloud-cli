**Example 1:  获取固件列表示例**



Input: 

```
tccli iotcloud ListFirmwares --cli-unfold-argument  \
    --ProductId abc \
    --PageNum 1 \
    --PageSize 1 \
    --Filters.0.Key abc \
    --Filters.0.Value abc
```

Output: 
```
{
    "Response": {
        "TotalCount": 1,
        "Firmwares": [
            {
                "Version": "abc",
                "Md5sum": "abc",
                "CreateTime": 1,
                "ProductName": "abc",
                "Name": "abc",
                "Description": "abc",
                "ProductId": "abc",
                "FwType": "abc",
                "CreateUserId": 1
            }
        ],
        "RequestId": "abc"
    }
}
```

