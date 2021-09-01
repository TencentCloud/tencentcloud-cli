**Example 1: 查询对账单下载地址正常示例**

查询对账单下载地址正常的示例

Input: 

```
tccli cpdp QueryDownloadBillURL --cli-unfold-argument  \
    --MerchantAppId 1c6f415798301d85fc4589a5435b54 \
    --ChannelCode ZSB2B \
    --BillDate 20211012
```

Output: 
```
{
    "Response": {
        "RequestId": "fd590936-acd7-440c-9ac5-b698bc0a5af0",
        "MerchantAppId": "1c6f41570498301d85fc4589a5435b54",
        "DownloadUrl": "http://xx.myqcloud.com/C000000198-20210723.xls"
    }
}
```

