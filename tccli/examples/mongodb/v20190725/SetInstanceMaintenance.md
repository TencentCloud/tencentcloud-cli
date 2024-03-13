**Example 1: 修改实例维护时间窗口**

修改实例维护时间窗口

Input: 

```
tccli mongodb SetInstanceMaintenance --cli-unfold-argument  \
    --InstanceId cmgo-9d0p**** \
    --MaintenanceEnd 21:00 \
    --MaintenanceStart 20:00
```

Output: 
```
{
    "Response": {
        "RequestId": "1df930fb-eb7e-4e3f-bcab-15a1aa5fede0"
    }
}
```

