**Example 1: 创建成功**



Input: 

```
tccli trocket CreateMigrationTask --cli-unfold-argument  \
    --InstanceId rmq-xxxx \
    --Type 1 \
    --Groups.0.InstanceId  \
    --Groups.0.ConsumerGroup iegt2i \
    --Groups.0.ConsumeEnable True \
    --Groups.0.ConsumeMessageOrderly True \
    --Groups.0.MaxRetryTimes 8 \
    --Groups.0.Remark  \
    --Groups.1.InstanceId  \
    --Groups.1.ConsumerGroup iegt1i \
    --Groups.1.ConsumeEnable True \
    --Groups.1.ConsumeMessageOrderly True \
    --Groups.1.MaxRetryTimes 16 \
    --Groups.1.Remark IEGT for Import Export Group Test
```

Output: 
```
{
    "Response": {
        "RequestId": "xxxx"
    }
}
```

