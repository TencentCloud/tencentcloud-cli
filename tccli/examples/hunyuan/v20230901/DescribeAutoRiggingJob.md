**Example 1: 调用示例**



Input: 

```
tccli hunyuan DescribeAutoRiggingJob --cli-unfold-argument  \
    --JobId 1440599109062270976
```

Output: 
```
{
    "Response": {
        "ErrorCode": "",
        "ErrorMessage": "",
        "ResultFile3Ds": [
            {
                "Type": "FBX",
                "Url": "https://**************************.cos.ap-singapore.tencentcos.cn/auto_rigging/output/251292921/99ebfc94-6914-4da5-9bc9-282dec6668f4_0.fbx?q-sign-algorithm=sha1&q-ak=************************************&q-sign-time=1777360055%3B1777446454&q-key-time=1777360055%3B1777446454&q-header-list=host&q-url-param-list=&q-signature=a3a7c84e18b90234e71f1d2236b4031a1a1122b6"
            }
        ],
        "Status": "DONE",
        "RequestId": "0c8fbea2-96d6-43a8-88da-c218d820eb1a"
    }
}
```

