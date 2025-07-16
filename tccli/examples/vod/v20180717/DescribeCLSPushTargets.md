**Example 1: 查询日志投递目标**



Input: 

```
tccli vod DescribeCLSPushTargets --cli-unfold-argument  \
    --Domains example.com
```

Output: 
```
{
    "Response": {
        "TotalCount": 1,
        "DomainCLSTargets": [
            {
                "Domain": "example.com",
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
        "RequestId": "12ae8d8e-dce3-4151-9d4b-5594145287e2"
    }
}
```

