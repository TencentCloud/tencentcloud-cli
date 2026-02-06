**Example 1: 设置实例属性**



Input: 

```
tccli ckafka ModifyRoutineMaintenanceTask --cli-unfold-argument  \
    --InstanceId ckafka-9jnejnb9 \
    --MaintenanceType RE_BALANCE \
    --MaintenanceSubtype INSTANCE_PARTITION_RE_BALANCE \
    --PlannedTime 79200 \
    --Status 1 \
    --Week 1,2,3,4,5,6,7
```

Output: 
```
{
    "Response": {
        "Result": {
            "ReturnCode": "0",
            "ReturnMessage": "success",
            "Data": {
                "FlowId": 0,
                "RouteDTO": {
                    "RouteId": 0
                }
            }
        },
        "RequestId": "fcfb7c89-3973-44f1-9a3e-a2811c67434e"
    }
}
```

