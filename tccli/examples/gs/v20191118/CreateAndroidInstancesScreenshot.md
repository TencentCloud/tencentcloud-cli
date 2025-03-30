**Example 1: 安卓实例截图**

安卓实例截图

Input: 

```
tccli gs CreateAndroidInstancesScreenshot --cli-unfold-argument  \
    --AndroidInstanceIds cai-abcd1234
```

Output: 
```
{
    "Response": {
        "RequestId": "9d287fa8-d66f-4dd8-b3c6-5bca07f6a162",
        "TaskSet": [
            {
                "AndroidInstanceId": "cai-abcd1234",
                "TaskId": "78bb4db4-fd51-454d-9ddb-2047db5b3ef6"
            }
        ]
    }
}
```

