**Example 1: 安装安卓实例应用**

安装安卓实例应用

Input: 

```
tccli gs InstallAndroidInstancesApp --cli-unfold-argument  \
    --AndroidInstanceIds cai-abcd1234 \
    --AndroidAppId apk-drkmskme \
    --AndroidAppVersion 1719564791910084130
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

