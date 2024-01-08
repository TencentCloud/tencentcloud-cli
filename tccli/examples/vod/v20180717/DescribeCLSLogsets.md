**Example 1: 查询点播创建的广州地区日志集**



Input: 

```
tccli vod DescribeCLSLogsets --cli-unfold-argument  \
    --CLSRegion ap-guangzhou
```

Output: 
```
{
    "Response": {
        "Logsets": [
            {
                "LogsetId": "54079098-61ea-48f9-8270-3b041a5d0150",
                "LogsetName": "vod_cdn_logset_cn"
            }
        ],
        "RequestId": "xxx"
    }
}
```

