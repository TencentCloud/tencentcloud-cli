**Example 1: 查询游戏服务器会话队列**



Input: 

```
tccli gse DescribeGameServerSessionQueues --cli-unfold-argument  \
    --Names queue2
```

Output: 
```
{
    "Response": {
        "GameServerSessionQueues": [
            {
                "Destinations": [
                    {
                        "DestinationArn": "qcs::gse:ap-shanghai:uin/100045346943:alias/alias-8whoa55z-reu7dfdfphl"
                    }
                ],
                "GameServerSessionQueueArn": "qcs::gse:ap-shanghai:uin/24353458499:queue/t2",
                "Name": "queue2",
                "PlayerLatencyPolicies": [
                    {
                        "MaximumIndividualPlayerLatencyMilliseconds": 56,
                        "PolicyDurationSeconds": 20
                    }
                ],
                "TimeoutInSeconds": 20
            }
        ],
        "RequestId": "3832851f-2b09-47dc-85db-27c33946456549",
        "TotalCount": 1
    }
}
```

