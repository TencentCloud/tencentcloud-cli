**Example 1: 创建中断会话的任务**



Input: 

```
tccli dbbrain CreateKillTask --cli-unfold-argument  \
    --InstanceId cdb-8jawylhf \
    --Product mysql \
    --Duration -1
```

Output: 
```
{
    "Response": {
        "Status": 1,
        "RequestId": "09299b00-b878-11eb-b0b4-959ba47770cf"
    }
}
```

