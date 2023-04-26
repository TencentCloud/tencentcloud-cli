**Example 1: 查询实例**

创建实例

Input: 

```
tccli rum CreateTawInstance --cli-unfold-argument  \
    --AreaId 1 \
    --InstanceName test \
    --ChargeType 1 \
    --DataRetentionDays 30 \
    --InstanceDesc test
```

Output: 
```
{
    "Response": {
        "InstanceId": "taw-4vVPH0Jn",
        "DealName": "",
        "RequestId": "57f4d8a2-13b6-4ac0-9f0b-0acc7bbc1d61"
    }
}
```

