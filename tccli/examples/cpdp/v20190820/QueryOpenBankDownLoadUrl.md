**Example 1: 查询对账单下载url成功示例**

查询对账单下载url成功示例

Input: 

```
tccli cpdp QueryOpenBankDownLoadUrl --cli-unfold-argument  \
    --ChannelMerchantId CM572433237990035456 \
    --BillDate 2020-10-08 \
    --ChannelName TENPAY \
    --PaymentMethod SAFT_ISV
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

