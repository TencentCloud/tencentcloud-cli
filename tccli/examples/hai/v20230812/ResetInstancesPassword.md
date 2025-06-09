**Example 1: 实例重置密码**

实例重置密码

Input: 

```
tccli hai ResetInstancesPassword --cli-unfold-argument  \
    --InstanceIds hai-xxxx \
    --DryRun False \
    --Password test#123456
```

Output: 
```
{
    "Response": {
        "RequestId": "e188f45e-e2db-4c30-81e0-2e7a3dfa7754",
        "TaskId": 232559186
    }
}
```

