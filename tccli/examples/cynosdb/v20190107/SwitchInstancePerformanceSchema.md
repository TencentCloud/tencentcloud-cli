**Example 1: 开启pfs**



Input: 

```
tccli cynosdb SwitchInstancePerformanceSchema --cli-unfold-argument  \
    --InstanceId cynosdbmysql-ins-6hwb9ix7 \
    --Operation enable \
    --Instruments wait/% \
    --Consumers events_waits_current \
    --CollectOperation enable
```

Output: 
```
{
    "Response": {
        "JobId": "24817776",
        "RequestId": "e72cd32c-45a1-40e8-a05e-667e3d06a9e6"
    }
}
```

