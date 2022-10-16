**Example 1: 拉取结果**



Input: 

```
tccli faceid GetSdkVerificationResult --cli-unfold-argument  \
    --SdkToken D2B55F0C-FB5D-4FB6-8765-3E931EBBFC79
```

Output: 
```
{
    "Response": {
        "CardVerifyResults": [
            {
                "IsPass": true,
                "CardVideo": {
                    "Url": "https://intl-reflect-h5-1257237511.cos.ap-guangzhou.myqcloud.com",
                    "MD5": "682e24b207acf1825286c1fceef5631c",
                    "Size": 9430792
                },
                "CardImage": {
                    "Url": "https://intl-reflect-h5-1257237511.cos.ap-guangzhou.myqcloud.com",
                    "MD5": "667c2448b10b09ee9ec14ab2b0d36608",
                    "Size": 232267
                },
                "CardInfoOcrJson": {
                    "Url": "https://intl-reflect-h5-1257237511.cos.ap-guangzhou.myqcloud.com",
                    "MD5": "0ae50935bb50cd70e6e34f81ff2e3fbd",
                    "Size": 224
                },
                "RequestId": "8e510d65-c26e-4de7-991d-e07ef0ad953d"
            }
        ],
        "CompareResults": [
            {
                "ErrorCode": "1001",
                "ErrorMsg": "Failed to call the liveness engine",
                "LiveData": {
                    "Url": "https://intl-reflect-h5-1257237511.cos.ap-guangzhou.myqcloud.com",
                    "MD5": "f624d26bfb45e149b293097037819feb",
                    "Size": 719585
                },
                "LiveVideo": {
                    "Url": "https://intl-reflect-h5-1257237511.cos.ap-guangzhou.myqcloud.com",
                    "MD5": "e87070d8eb95f64bc01b12e03cc8f533",
                    "Size": 887224
                },
                "LiveErrorCode": "1001",
                "LiveErrorMsg": "Failed to call the liveness engine",
                "CompareErrorCode": "",
                "CompareErrorMsg": "",
                "BestFrame": {
                    "Url": "https://intl-reflect-h5-1257237511.cos.ap-guangzhou.myqcloud.com",
                    "MD5": "c4f217871aaeb0180e40152f61658835",
                    "Size": 122984
                },
                "ProfileImage": {
                    "Url": "https://intl-reflect-h5-1257237511.cos.ap-guangzhou.myqcloud.com",
                    "MD5": "d51df99b25d87785ea5e2dfb0d6e920f",
                    "Size": 23091
                },
                "Sim": 0,
                "IsNeedCharge": true,
                "CardInfoInputJson": {
                    "Url": "https://intl-reflect-h5-1257237511.cos.ap-guangzhou.myqcloud.com",
                    "MD5": "02497f445dc72a330b468fa24529315b",
                    "Size": 219
                },
                "RequestId": "6e498069-4d51-4032-82a8-9adb53cda85b"
            }
        ],
        "ChargeCount": 4,
        "Description": "Failed to call the liveness engine",
        "Extra": "",
        "RequestId": "b8cb2269-08b2-426c-8be8-c7142c7e64e4",
        "Result": "1001"
    }
}
```

