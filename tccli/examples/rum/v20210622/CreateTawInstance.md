**Example 1: 查询实例**

创建实例

Input: 

```
tccli rum CreateTawInstance --cli-unfold-argument  \
    --AreaId 1 \
    --InstanceName ****VPH0Jn \
    --ChargeType 1 \
    --DataRetentionDays 30 \
    --InstanceDesc 业务系统
```

Output: 
```
{
    "Response": {
        "InstanceId": "****VPH0Jn",
        "DealName": "****3459432",
        "RequestId": "57f4d8a2-13b6-4ac0-9f0b-0acc7bbc1d61"
    }
}
```

