**Example 1: 查询安卓实例黑名单示例**



Input: 

```
tccli gs DescribeAndroidInstancesAppBlacklist --cli-unfold-argument  \
    --AndroidInstanceIds cai-wsczvffa
```

Output: 
```
{
    "Response": {
        "AppBlacklistSet": [
            {
                "AndroidInstanceId": "cai-asgrsda",
                "AppBlacklist": [
                    "com-acc"
                ]
            }
        ],
        "RequestId": "ef4d4555-cddc-4c42-b0ac-528bdb7a94e5"
    }
}
```

