**Example 1: 范例**



Input: 

```
tccli wedata RerunInstances --cli-unfold-argument  \
    --DependentWay 1 \
    --ProjectId 1 \
    --RerunType 1 \
    --Instances.0.TaskId 20220711143109589 \
    --Instances.0.CurRunDate 2022-07-22 00:00:00 \
    --SonInstanceType 1 \
    --CheckFather false \
    --SkipEventListening false
```

Output: 
```
{
    "Response": {
        "RequestId": "29a6fb64-135b-4151-b12a-c4881889071b",
        "Data": {
            "Result": true,
            "ErrorId": null,
            "ErrorDesc": null
        }
    }
}
```

