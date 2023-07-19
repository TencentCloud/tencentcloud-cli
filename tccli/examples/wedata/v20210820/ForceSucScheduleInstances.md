**Example 1: test**

test

Input: 

```
tccli wedata ForceSucScheduleInstances --cli-unfold-argument  \
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
        "RequestId": "03e9a01a-53c3-4660-88b3-b1465d1a3610"
    }
}
```

