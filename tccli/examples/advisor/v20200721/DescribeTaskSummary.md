**Example 1: 查询任务执行的结果总览**



Input: 

```
tccli advisor DescribeTaskSummary --cli-unfold-argument  \
    --TaskId e9ea4f2a-98c5-47ed-9706-a7446a06ad1a
```

Output: 
```
{
    "Response": {
        "FinishTime": "2020-09-22T00:00:00+00:00",
        "IsFinish": true,
        "RequestId": "xx",
        "StrategySummaries": [
            {
                "Count": 1,
                "Code": "xx",
                "LowRiskCount": 1,
                "HighRiskCount": 1,
                "IgnoredInstanceCount": 1,
                "StrategyName": "xx",
                "StrategyId": 1,
                "GroupId": 1,
                "MediumRiskCount": 1,
                "NoRiskCount": 1
            },
            {
                "Count": 1,
                "Code": "xx",
                "MediumRiskCount": 0,
                "LowRiskCount": 0,
                "HighRiskCount": 0,
                "IgnoredInstanceCount": 0,
                "NoRiskCount": 0,
                "StrategyId": 2,
                "GroupId": 1,
                "StrategyName": "xx"
            },
            {
                "Count": 1,
                "Code": "xx",
                "MediumRiskCount": 1,
                "LowRiskCount": 1,
                "HighRiskCount": 1,
                "IgnoredInstanceCount": 1,
                "NoRiskCount": 1,
                "StrategyId": 3,
                "GroupId": 2,
                "StrategyName": "xx"
            },
            {
                "Count": 1,
                "Code": "xx",
                "MediumRiskCount": 1,
                "LowRiskCount": 1,
                "HighRiskCount": 1,
                "IgnoredInstanceCount": 1,
                "NoRiskCount": 1,
                "StrategyId": 4,
                "GroupId": 2,
                "StrategyName": "xx"
            },
            {
                "Count": 1,
                "Code": "xx",
                "MediumRiskCount": 1,
                "LowRiskCount": 1,
                "HighRiskCount": 1,
                "IgnoredInstanceCount": 1,
                "NoRiskCount": 1,
                "StrategyId": 5,
                "GroupId": 3,
                "StrategyName": "xx"
            },
            {
                "Count": 1,
                "Code": "xx",
                "MediumRiskCount": 1,
                "LowRiskCount": 1,
                "HighRiskCount": 1,
                "IgnoredInstanceCount": 1,
                "NoRiskCount": 1,
                "StrategyId": 6,
                "GroupId": 3,
                "StrategyName": "xx"
            },
            {
                "Count": 1,
                "Code": "xx",
                "MediumRiskCount": 1,
                "LowRiskCount": 1,
                "HighRiskCount": 1,
                "IgnoredInstanceCount": 1,
                "NoRiskCount": 1,
                "StrategyId": 7,
                "GroupId": 4,
                "StrategyName": "xx"
            },
            {
                "Count": 1,
                "Code": "xx",
                "MediumRiskCount": 1,
                "LowRiskCount": 1,
                "HighRiskCount": 1,
                "IgnoredInstanceCount": 1,
                "NoRiskCount": 1,
                "StrategyId": 8,
                "GroupId": 4,
                "StrategyName": "xx"
            },
            {
                "Count": 1,
                "Code": "xx",
                "MediumRiskCount": 1,
                "LowRiskCount": 1,
                "HighRiskCount": 1,
                "IgnoredInstanceCount": 1,
                "NoRiskCount": 1,
                "StrategyId": 9,
                "GroupId": 5,
                "StrategyName": "xx"
            },
            {
                "Count": 1,
                "Code": "xx",
                "MediumRiskCount": 1,
                "LowRiskCount": 1,
                "HighRiskCount": 1,
                "IgnoredInstanceCount": 1,
                "NoRiskCount": 1,
                "StrategyId": 10,
                "GroupId": 5,
                "StrategyName": "xx"
            },
            {
                "Count": 1,
                "Code": "xx",
                "MediumRiskCount": 1,
                "LowRiskCount": 1,
                "HighRiskCount": 0,
                "IgnoredInstanceCount": 1,
                "NoRiskCount": 1,
                "StrategyId": 11,
                "GroupId": 1,
                "StrategyName": "xx"
            },
            {
                "Count": 1,
                "Code": "xx",
                "MediumRiskCount": 0,
                "LowRiskCount": 1,
                "HighRiskCount": 0,
                "IgnoredInstanceCount": 1,
                "NoRiskCount": 1,
                "StrategyId": 12,
                "GroupId": 1,
                "StrategyName": "xx"
            },
            {
                "Count": 1,
                "Code": "xx",
                "MediumRiskCount": 0,
                "LowRiskCount": 0,
                "HighRiskCount": 0,
                "IgnoredInstanceCount": 1,
                "NoRiskCount": 1,
                "StrategyId": 13,
                "GroupId": 1,
                "StrategyName": "xx"
            }
        ],
        "GroupSummaries": [
            {
                "MediumRiskCount": 0,
                "LowRiskCount": 0,
                "GroupId": 2,
                "NoRiskCount": 0,
                "HighRiskCount": 2
            },
            {
                "MediumRiskCount": 0,
                "LowRiskCount": 0,
                "GroupId": 3,
                "NoRiskCount": 0,
                "HighRiskCount": 2
            },
            {
                "MediumRiskCount": 0,
                "LowRiskCount": 0,
                "GroupId": 4,
                "NoRiskCount": 0,
                "HighRiskCount": 2
            },
            {
                "MediumRiskCount": 0,
                "LowRiskCount": 0,
                "GroupId": 5,
                "NoRiskCount": 0,
                "HighRiskCount": 2
            },
            {
                "MediumRiskCount": 1,
                "LowRiskCount": 1,
                "GroupId": 1,
                "NoRiskCount": 1,
                "HighRiskCount": 1
            },
            {
                "MediumRiskCount": 1,
                "LowRiskCount": 1,
                "GroupId": 0,
                "NoRiskCount": 1,
                "HighRiskCount": 9
            }
        ],
        "TaskId": "xx",
        "Has": true,
        "CreateTime": "2020-09-22T00:00:00+00:00",
        "LastSuccessTaskId": "xx"
    }
}
```

