**Example 1: hai实例关机**

hai实例关机不收费场景。

Input: 

```
tccli hai StopInstance --cli-unfold-argument  \
    --InstanceId hai-dunyfddn \
    --StopMode STOP_CHARGE \
    --DryRun False
```

Output: 
```
{
    "Response": {
        "TaskId": 123456,
        "RequestId": "057b40b9-c27f-4241-918b-debd34cfdafdasfdaf"
    }
}
```

