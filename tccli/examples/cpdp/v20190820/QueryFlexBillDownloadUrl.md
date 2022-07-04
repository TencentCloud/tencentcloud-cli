**Example 1: 查询对账单文件下载链接**



Input: 

```
tccli cpdp QueryFlexBillDownloadUrl --cli-unfold-argument  \
    --BillDate 2022-06-22 \
    --BillType FREEZE \
    --ServiceProviderId 
```

Output: 
```
{
    "Response": {
        "ErrCode": "SUCCESS",
        "ErrMessage": "成功",
        "Result": {
            "Url": "xxxxx",
            "ExpireTime": "2022-06-07 00:00:00"
        },
        "RequestId": "8ffecac1-2d89-43a9-9075-a985442ef466"
    }
}
```

