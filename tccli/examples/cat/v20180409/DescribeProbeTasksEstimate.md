**Example 1: 对新建的拨测任务进行价格估算**



Input: 

```
tccli cat DescribeProbeTasksEstimate --cli-unfold-argument  \
    --BatchTasks.0.Name probe \
    --BatchTasks.0.TargetAddress http://www.baidu.com \
    --Parameters {} \
    --Interval 30 \
    --TaskCategory 1 \
    --TaskType 1 \
    --Nodes 10001 \
    --Cron * 0-6 * * * \
    --HourTimeSpan 720
```

Output: 
```
{
    "Response": {
        "TotalCost": 155520,
        "AdvanceNum": 0.0,
        "RealTotalCost": 155520,
        "HourTimeSpan": 720,
        "BaseNum": 0.0,
        "RequestId": "abc"
    }
}
```

