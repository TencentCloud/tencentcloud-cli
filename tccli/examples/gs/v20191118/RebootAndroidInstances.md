**Example 1: 重启安卓实例**

重启安卓实例

Input: 

```
tccli gs RebootAndroidInstances --cli-unfold-argument  \
    --AndroidInstanceIds xxx
```

Output: 
```
{
    "Response": {
        "RequestId": "6f7b34a3-0c00-4fac-b6f0-08d47ac3e736",
        "TaskSet": [
            {
                "TaskId": "abc",
                "AndroidInstanceId": "abc"
            }
        ]
    }
}
```

