**Example 1: 修改指定日志类别投递配置、开关**



Input: 

```
tccli cwp ModifyLogKafkaDeliverType --cli-unfold-argument  \
    --SecurityType 1 \
    --LogType 1 2 \
    --Switch 1 \
    --TopicId topic-xdd*** \
    --TopicName n
```

Output: 
```
{
    "Response": {
        "RequestId": "c"
    }
}
```

