**Example 1: 批量查询安装指定应用的安卓实例**



Input: 

```
tccli gs DescribeAndroidInstancesByApps --cli-unfold-argument  \
    --Offset 0 \
    --Limit 100 \
    --AndroidAppIds apk-abcd1234
```

Output: 
```
{
    "Response": {
        "RequestId": "6f7b34a3-0c00-4fac-b6f0-08d47ac3e736",
        "TotalCount": 1,
        "AndroidInstances": [
            {
                "AndroidInstanceId": "cai-abcd1234",
                "AndroidInstanceRegion": "ap-guagnzhou",
                "State": "NORMAL",
                "AndroidInstanceType": "A6"
            }
        ]
    }
}
```

