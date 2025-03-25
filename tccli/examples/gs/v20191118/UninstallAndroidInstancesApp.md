**Example 1: 卸载安卓实例应用**

卸载安卓实例应用

Input: 

```
tccli gs UninstallAndroidInstancesApp --cli-unfold-argument  \
    --AndroidInstanceIds cai-abcd-1234 \
    --AndroidAppId apk-drkmskme
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

