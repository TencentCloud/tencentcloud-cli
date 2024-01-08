**Example 1: 查询日志投递目标**



Input: 

```
tccli vod DescribeCLSPushTargets --cli-unfold-argument  \
    --Domains xxx.vod-qcloud.com
```

Output: 
```
{
    "Response": {
        "TotalCount": 1,
        "DomainCLSTargets": [
            {
                "Domain": "xxx.vod-qcloud.com",
                "ChineseMainlandCLSTargetInfo": {
                    "Switch": "OFF",
                    "CLSRegion": "ap-guangzhou",
                    "TopicId": "",
                    "LogsetId": ""
                },
                "OutsideChineseMainlandCLSTargetInfo": {
                    "Switch": "OFF",
                    "CLSRegion": "ap-singapore",
                    "TopicId": "",
                    "LogsetId": ""
                }
            }
        ],
        "RequestId": "xxx"
    }
}
```

