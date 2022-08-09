**Example 1: 范例**



Input: 

```
tccli wedata KillInstances --cli-unfold-argument  \
    --ProjectId 1 \
    --Instances.0.TaskId 20220711143109589 \
    --Instances.0.CurRunDate 2022-07-22 00:00:00
```

Output: 
```
{
    "Response": {
        "RequestId": "1c3bc2b3-ba5e-4bd9-9a74-88a84c996eba",
        "Data": {
            "Result": true,
            "ErrorId": null,
            "ErrorDesc": null
        }
    }
}
```

