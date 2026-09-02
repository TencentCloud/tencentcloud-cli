**Example 1: 执行变配**



Input: 

```
tccli tcb ModifyPGInstanceSpec --cli-unfold-argument  \
    --EnvId *****-****-d7gpxb78091c30209 \
    --Cpu 1 \
    --Memory 2 \
    --Storage 30 \
    --SwitchTag 1 \
    --SwitchStartTime 2026-08-26 20:15:00 \
    --SwitchEndTime 2026-08-26 21:15:00 \
    --DryRun False
```

Output: 
```
{
    "Response": {
        "BillId": "219429",
        "DealName": "",
        "RequestId": "4bcb1dba-5360-4c46-a8b5-5406958ebc72"
    }
}
```

