**Example 1: 更新拨测任务配置**



Input: 

```
tccli cat UpdateProbeTaskConfigurationList --cli-unfold-argument  \
    --TaskIds task-xx \
    --Interval 30 \
    --Nodes 10001 \
    --Parameters {} \
    --Cron * 0-6 * * *
```

Output: 
```
{
    "Response": {
        "RequestId": "abc"
    }
}
```

