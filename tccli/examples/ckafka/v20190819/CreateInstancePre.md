**Example 1: 创建实例(预付费包年包月)**



Input: 

```
tccli ckafka CreateInstancePre --cli-unfold-argument  \
    --InstanceName test \
    --MsgRetentionTime 1440 \
    --InstanceType 1 \
    --ZoneId 100003 \
    --Period 1m
```

Output: 
```
{
    "Response": {}
}
```

