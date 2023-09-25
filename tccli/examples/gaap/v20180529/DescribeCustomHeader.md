**Example 1: 查询自定义header列表**



Input: 

```
tccli gaap DescribeCustomHeader --cli-unfold-argument  \
    --RuleId rule-18vhg67
```

Output: 
```
{
    "Response": {
        "RequestId": "c7bfcad5-3f20-472f-9afc-13a66faebad8",
        "RuleId": "rule-18vhg67",
        "Headers": [
            {
                "HeaderName": "X-REAL_IP",
                "HeaderValue": "$remote_addr"
            },
            {
                "HeaderName": "X-FORWORD-IP",
                "HeaderValue": "192.168.2.101"
            }
        ]
    }
}
```

