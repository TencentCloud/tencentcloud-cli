**Example 1: 示例**

获取巡课列表

Input: 

```
tccli lcic DescribeSupervisors --cli-unfold-argument  \
    --SdkAppId 1 \
    --Limit 1 \
    --Page 1
```

Output: 
```
{
    "Response": {
        "Total": 1,
        "Page": 1,
        "Limit": 1,
        "UserIds": [
            "abc"
        ],
        "RequestId": "abc"
    }
}
```

