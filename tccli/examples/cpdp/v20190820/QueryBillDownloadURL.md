**Example 1: QueryBillDownloadURL**



Input: 

```
tccli cpdp QueryBillDownloadURL --cli-unfold-argument  \
    --TransferType 3 \
    --BillDate 2020-12-18 \
    --MerchantId faryrong
```

Output: 
```
{
    "Response": {
        "RequestId": "CPDP-1609296532884",
        "ErrMessage": "成功",
        "ErrCode": "SUCCESS",
        "Result": {
            "OriginalBillDownloadURL": "http://cpdp-transfer-1258344699.cos.ap-nanjing.myqcloud.com/transfer/faryrong/2020-12-18.csv?sign=q-sign-algorithm%3Dsha1%26q-ak%3DAKIDxiQKyTvz1pRJ1UtxvdCZooZ72pTwoE4f%26q-sign-time%3D1609296546%3B1609300146%26q-key-time%3D1609296546%3B1609300146%26q-header-list%3D%26q-url-param-list%3D%26q-signature%3D272b429cdd2a0127ea8ce377a155df13655b6ef9",
            "BillDownloadURL": "http://cpdp-transfer-1258344699.cos.ap-nanjing.myqcloud.com/smart_transfer/pingan/gen/faryrong_2020-12-18.csv?sign=q-sign-algorithm%3Dsha1%26q-ak%3DAKIDxiQKyTvz1pRJ1UtxvdCZooZ72pTwoE4f%26q-sign-time%3D1609296548%3B1609300148%26q-key-time%3D1609296548%3B1609300148%26q-header-list%3D%26q-url-param-list%3D%26q-signature%3D29d65b284e5d3d80c7326e02760e66848dead104"
        }
    }
}
```

