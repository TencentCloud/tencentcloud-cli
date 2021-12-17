**Example 1: 批量创建探测任务**



Input: 

```
tccli cat CreateProbeTasks --cli-unfold-argument  \
    --BatchTasks.0.Name probe \
    --BatchTasks.0.TargetAddress http://www.baidu.com \
    --Parameters {} \
    --Interval 30 \
    --TaskCategory 1 \
    --TaskType 1 \
    --Nodes 10001 \
    --Cron * 0-6 * * *
```

Output: 
```
{
    "Response": {
        "RequestId": "xx"
    }
}
```

