**Example 1: 更新维护时间窗口**



Input: 

```
tccli cdb ModifyTimeWindow --cli-unfold-argument  \
    --InstanceId cdb-eb2w7dto \
    --TimeRanges 03:00-03:30 \
    --Weekdays monday \
    --MaxDelayTime 10
```

Output: 
```
{
    "Response": {
        "RequestId": "1a42feb9-82087f71-6a0031ac-699a92a8"
    }
}
```

