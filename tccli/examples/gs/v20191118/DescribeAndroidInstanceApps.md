**Example 1: 查询安卓实例应用**

查询安卓实例应用

Input: 

```
tccli gs DescribeAndroidInstanceApps --cli-unfold-argument  \
    --AndroidInstanceId xxx
```

Output: 
```
{
    "Response": {
        "RequestId": "6f7b34a3-0c00-4fac-b6f0-08d47ac3e736",
        "Apps": [
            {
                "AndroidAppId": "apk-nm5r03gm",
                "Name": "测试2",
                "AndroidAppVersion": "xxx"
            },
            {
                "AndroidAppId": "apk-qekh35py",
                "Name": "does",
                "AndroidAppVersion": "xxx"
            }
        ]
    }
}
```

