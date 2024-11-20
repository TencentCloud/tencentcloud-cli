**Example 1: 获取伸缩组全局配置**



Input: 

```
tccli emr DescribeAutoScaleGroupGlobalConf --cli-unfold-argument  \
    --InstanceId emr-123
```

Output: 
```
{
    "Response": {
        "GroupGlobalConfs": [
            {
                "CurrentNodes": 0,
                "CurrentPostPaidNodes": 0,
                "CurrentSpotPaidNodes": 0,
                "GroupGlobalConf": {
                    "ChangeToPod": 0,
                    "ClusterId": 33003386,
                    "EnableMNode": 0,
                    "GraceDownFlag": true,
                    "GroupName": "回归group-002",
                    "GroupStatus": 2,
                    "HardwareType": "HOST",
                    "Id": 26,
                    "NextTimeCanScale": 0,
                    "Parallel": 1,
                    "PayMode": "POSTPAY",
                    "PostPayPercentMin": 0,
                    "ScaleLowerBound": 0,
                    "ScaleUpperBound": 30,
                    "StrategyType": 0
                }
            }
        ],
        "RequestId": "4dea2795-c996-4385-88f8-c6191766e519",
        "TotalCount": 1
    }
}
```

