**Example 1: UpgradePGInstanceToDedicated**



Input: 

```
tccli tcb UpgradePGInstanceToDedicated --cli-unfold-argument  \
    --EnvId *****r-****8g1j2dbc0df14561 \
    --SwitchTag 1 \
    --SwitchStartTime 15:04:05 \
    --SwitchEndTime 15:04:05 \
    --SpecCode pg.it.small2 \
    --Storage 10
```

Output: 
```
{
    "Response": {
        "TaskId": "task-sdffs",
        "RequestId": "d6243aeb-67b2-483b-893b-d264361f6afd"
    }
}
```

