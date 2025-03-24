**Example 1: 安装安卓实例应用**

安装安卓实例应用

Input: 

```
tccli gs InstallAndroidInstancesApp --cli-unfold-argument  \
    --AndroidInstanceIds xxx \
    --AndroidAppId xxx \
    --AndroidAppVersion xxx
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

