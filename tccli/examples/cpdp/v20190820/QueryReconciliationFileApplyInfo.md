**Example 1: 聚鑫-查询对账文件申请结果-成功**



Input: 

```
tccli cpdp QueryReconciliationFileApplyInfo --cli-unfold-argument  \
    --ApplyFileId 20220303181840234585170504588894208
```

Output: 
```
{
    "Response": {
        "RequestId": "102b8eeb-689f-4e06-b1c1-96b752cf204c",
        "Result": {
            "ApplyFileId": "20220303181840234585170504588894208",
            "ApplyStatus": "S",
            "ApplyMessage": "申请成功",
            "FileUrlArray": [
                "https://snake-account-dev-1258344699.cos.ap-guangzhou.myqcloud.com/20220303181840234585170504588894208-YE2022030220311.txt?sign=q-sign-algorithm%3Dsha1%26q-ak%3DAKIDxiQKyTvz1pRJ1UtxvdCZooZ72pTwoE4f%26q-sign-time%3D1646302788%3B1646389188%26q-key-time%3D1646302788%3B1646389188%26q-header-list%3D%26q-url-param-list%3D%26q-signature%3De28ee3331305fd6db5884675d0d161fbc307858b"
            ]
        },
        "ErrCode": "SUCCESS",
        "ErrMessage": "成功"
    }
}
```

