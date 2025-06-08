**Example 1: 修改安卓实例应用黑名单示例**



Input: 

```
tccli gs ModifyAndroidInstancesAppBlacklist --cli-unfold-argument  \
    --AndroidInstanceIds cai-xxx \
    --Operation ADD \
    --AppList com.acc
```

Output: 
```
{
    "Response": {
        "TaskSet": [
            {
                "TaskId": "ef4d4555-cddc-4c42-b0ac-528bdb7a94e5"
            }
        ],
        "RequestId": "ef4d4555-cddc-4c42-b0ac-528bdb7a94e5"
    }
}
```

