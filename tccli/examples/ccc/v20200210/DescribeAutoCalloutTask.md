**Example 1: 查询任务**



Input: 

```
tccli ccc DescribeAutoCalloutTask --cli-unfold-argument  \
    --SdkAppId 1 \
    --TaskId 2
```

Output: 
```
{
    "Response": {
        "IvrId": 1,
        "Name": "xx",
        "NotBefore": 1,
        "NotAfter": 0,
        "State": 1,
        "Callers": [
            "008610086"
        ],
        "RequestId": "xx",
        "Callees": [
            {
                "State": 1,
                "Callee": "xx"
            }
        ],
        "Description": "xx"
    }
}
```

