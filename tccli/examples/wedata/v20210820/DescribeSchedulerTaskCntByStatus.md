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
                "CountTag": 0,
                "DayNum": 0,
                "FrozenNum": 0,
                "HourNum": 0,
                "InvalidNum": 0,
                "MinuteNum": 0,
                "MonthNum": 0,
                "RunningNum": 0,
                "StoppedNum": 0,
                "StoppingNum": 0,
                "TotalNum": 0,
                "WeekNum": 0,
                "YearNum": 0
            }
        ],
        "RequestId": "717516e8-fece-4821-850b-43b4379c816d"
    }
}
```

