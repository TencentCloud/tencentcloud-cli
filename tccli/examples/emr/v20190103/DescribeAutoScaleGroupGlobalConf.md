**Example 1: 获取伸缩组全局配置**



Input: 

```
tccli emr DescribeAutoScaleGroupGlobalConf --cli-unfold-argument  \
    --InstanceId abc
```

Output: 
```
{
    "Response": {
        "GroupGlobalConfs": [
            {
                "GroupGlobalConf": {
                    "Id": 0,
                    "ClusterId": 0,
                    "ScaleLowerBound": 0,
                    "ScaleUpperBound": 0,
                    "StrategyType": 0,
                    "NextTimeCanScale": 1,
                    "GraceDownFlag": true,
                    "HardwareType": "abc",
                    "PayMode": "abc",
                    "PostPayPercentMin": 0,
                    "ChangeToPod": 0,
                    "GroupName": "abc",
                    "YarnNodeLabel": "abc",
                    "GroupStatus": 0
                },
                "CurrentNodes": 0,
                "CurrentPostPaidNodes": 0,
                "CurrentSpotPaidNodes": 0
            }
        ],
        "TotalCount": 0,
        "RequestId": "abc"
    }
}
```

