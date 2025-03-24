**Example 1: 卸载安卓实例应用**

卸载安卓实例应用

Input: 

```
tccli gs UninstallAndroidInstancesApp --cli-unfold-argument  \
    --AndroidInstanceIds xxx \
    --AndroidAppId xxx
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

