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
        "DownloadUrl": "https://batch-productions-*************d37cbc7f2",
        "GenerationMethod": 0,
        "RequestId": "rest-clieet20111026",
        "UploadUrl": ""
    }
}
```

