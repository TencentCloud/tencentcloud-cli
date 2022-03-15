**Example 1: 查询对账单下载url成功示例**

查询对账单下载url成功示例

Input: 

```
tccli cpdp QueryOpenBankDownLoadUrl --cli-unfold-argument  \
    --ChannelMerchantId CM572433237990035456 \
    --BillDate 2020-10-08 \
    --BillType TRADE
```

Output: 
```
{
    "Response": {
        "RequestId": "171304d7-1084-4c98-9baa-fa1e8d2af7d0",
        "ErrCode": "SUCCESS",
        "ErrMessage": "成功",
        "Result": {
            "DownloadUrl": "https://xxx.cloud.xxx.com/finance/api/billdownload/file?token=xxx",
            "HashValue": "79bb0f45fc4c42234a918000b2668d689e2bde04",
            "HashType": "SHA256"
        }
    }
}
```

**Example 2: 查询账单下载成功示例**



Input: 

```
tccli cpdp QueryOpenBankDownLoadUrl --cli-unfold-argument  \
    --BillType TRADE \
    --BillDate 2022-02-12 \
    --ChannelMerchantId CM572433237990035456
```

Output: 
```
{
    "Response": {
        "RequestId": "0de6aef6-4e1d-463e-a793-057491ca1bcf",
        "Result": {
            "DownloadUrl": "",
            "HashValue": "",
            "HashType": ""
        },
        "ErrCode": "SUCCESS",
        "ErrMessage": "成功"
    }
}
```

**Example 3: 下载成功的示例**



Input: 

```
tccli cpdp QueryOpenBankDownLoadUrl --cli-unfold-argument  \
    --Environment 字符串 \
    --BillType 字符串 \
    --BillDate 字符串 \
    --ChannelMerchantId 字符串
```

Output: 
```
{
    "Response": {
        "RequestId": "f2fe8f90-667d-4593-a57f-c345e69af8b2",
        "Result": {
            "DownloadUrl": "",
            "HashValue": "",
            "HashType": ""
        },
        "ErrCode": "SUCCESS",
        "ErrMessage": "成功"
    }
}
```

