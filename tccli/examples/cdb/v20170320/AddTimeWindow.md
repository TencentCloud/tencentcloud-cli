**Example 1: 添加维护时间窗口**



Input: 

```
tccli cdb AddTimeWindow --cli-unfold-argument  \
    --InstanceId cdb-eb2w7dto \
    --Monday 02:00-03:00 \
    --MaxDelayTime 10
```

Output: 
```
{
    "Response": {
        "RequestId": "6EF60BEC-0242-43AF-BB20-270359FB54A7"
    }
}
```

