**Example 1: 任务状态统计示例**

任务状态统计

Input: 

```
tccli wedata DescribeSchedulerTaskCntByStatus --cli-unfold-argument  \
    --ProjectId 12312
```

Output: 
```
{
    "Response": {
        "Data": [
            {
                "CountTag": 1,
                "TotalNum": 1,
                "RunningNum": 1,
                "StoppingNum": 1,
                "StoppedNum": 1,
                "FrozenNum": 1,
                "YearNum": 1,
                "MonthNum": 1,
                "WeekNum": 1,
                "DayNum": 1,
                "HourNum": 1,
                "MinuteNum": 1
            }
        ],
        "RequestId": "abc"
    }
}
```

