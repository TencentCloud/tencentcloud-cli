**Example 1: 获取量产详情**



Input: 

```
tccli iotexplorer DescribeBatchProduction --cli-unfold-argument  \
    --ProductId R32ONVL0EU \
    --BatchProductionId LC-ya6zinv9
```

Output: 
```
{
    "Response": {
        "BatchCnt": 3,
        "BurnMethod": 0,
        "CreateTime": 1572233486,
        "DownloadUrl": "https://batch-productions-test-1256872341.cos.ap-guangzhou.myqcloud.com/100000546882%2FR32ONVL0EU_LC-6mgj9akp.csv?sign=q-sign-algorithm%3Dsha1%26q-ak%3DAKIDMUM9hdmn35rHZe72Y6UfliNo1PYQFZln%26q-sign-time%3D1572233867%3B1572234767%26q-key-time%3D1572233867%3B1572234767%26q-header-list%3D%26q-url-param-list%3D%26q-signature%3Da31f6ed1e25d3dc753516b74ee33559d37cbc7f2",
        "GenerationMethod": 0,
        "RequestId": "rest-clieet20111026",
        "UploadUrl": ""
    }
}
```

