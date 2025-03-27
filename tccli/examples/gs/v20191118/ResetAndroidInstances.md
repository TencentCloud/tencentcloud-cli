**Example 1: 重置安卓实例**

重置安卓实例

Input: 

```
tccli gs ResetAndroidInstances --cli-unfold-argument  \
    --AndroidInstanceIds cai-abcd1234
```

Output: 
```
{
    "Response": {
        "RequestId": "6f7b34a3-0c00-4fac-b6f0-08d47ac3e736",
        "TaskSet": [
            {
                "TaskId": "615cf0a4-075e-4cf5-b26f-d786363daccd",
                "AndroidInstanceId": "cai-abcd1234"
            }
        ]
    }
}
```

