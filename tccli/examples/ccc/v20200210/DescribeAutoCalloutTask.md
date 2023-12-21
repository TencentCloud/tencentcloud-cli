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
        "Name": "foobar",
        "NotBefore": 1,
        "NotAfter": 0,
        "State": 1,
        "Callers": [
            "008610086"
        ],
        "RequestId": "foobar",
        "Callees": [
            {
                "State": 1,
                "Callee": "foobar",
                "Sessions": [
                    "foobar"
                ]
            }
        ],
        "Description": "foobar"
    }
}
```

