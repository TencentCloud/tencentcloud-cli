**Example 1: 批量终止实例**

实例运维-批量终止实例

Input: 

```
tccli wedata KillScheduleInstances --cli-unfold-argument  \
    --ProjectId 1460947878944567296 \
    --Instances.0.TaskId 20230313145539749 \
    --Instances.0.CurRunDate 2023-03-13 14:55:53
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
        "RequestId": "7ac627e0-4ebf-4127-a3f0-a2d82c64f0e3"
    }
}
```

