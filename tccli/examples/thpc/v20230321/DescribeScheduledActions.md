**Example 1: 按照队列查询定时任务配置**



Input: 

```
tccli thpc DescribeScheduledActions --cli-unfold-argument  \
    --ClusterId hpc-brv22s4t \
    --QueueName thpc-as
```

Output: 
```
{
    "Response": {
        "RequestId": "d8a16885-b53d-4392-bfae-6622da419431"
    }
}
```

**Example 2: 按照集群查询定时任务配置**



Input: 

```
tccli thpc DescribeScheduledActions --cli-unfold-argument  \
    --ClusterId hpc-brv22s4t
```

Output: 
```
{
    "Response": {
        "RequestId": "2bb70350-b162-427e-99cf-78b465277563"
    }
}
```

