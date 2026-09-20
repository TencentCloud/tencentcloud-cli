**Example 1: DescribeAppStatisticsOverview 查询用户详情**



Input: 

```
tccli adp DescribeAppStatisticsOverview --cli-unfold-argument  \
    --AppType 1 \
    --TimeRange.EndTime 1789487999 \
    --TimeRange.StartTime 1789401600 \
    --ViewScope.ViewType 3 \
    --ViewScope.ScopeId 2099767969573745984 \
    --SpaceId default_space \
    --AppId 2099767969573745984
```

Output: 
```
{
    "Response": {
        "AvgFirstTokenTime": "0",
        "AvgTotalTokenTime": "0",
        "CallSuccessRate": 0,
        "ReplyTypeDistributionList": [
            {
                "CallCount": "0",
                "Percentage": 0,
                "ReplyName": "问答直接回复"
            }
        ],
        "TotalCallCount": "0",
        "RequestId": "5f6d2237-9741-4788-b442-56feb1022bab"
    }
}
```

