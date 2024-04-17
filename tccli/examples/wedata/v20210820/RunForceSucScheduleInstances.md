**Example 1: 实例批量置成功**

实例运维-实例批量置成功

Input: 

```
tccli wedata RunForceSucScheduleInstances --cli-unfold-argument  \
    --ProjectId 148541567890667712 \
    --Instances.0.TaskId 20240307215220701 \
    --Instances.0.CurRunDate 2024-04-09 00:00:00 \
    --Instances.1.TaskId 20240307221158488 \
    --Instances.1.CurRunDate 2024-04-09 00:00:00
```

Output: 
```
{
    "Response": {
        "Data": {
            "ErrorDesc": null,
            "ErrorId": null,
            "Result": true
        },
        "RequestId": "1d287884-1214-4b75-b4e8-383ee8e57918"
    }
}
```

