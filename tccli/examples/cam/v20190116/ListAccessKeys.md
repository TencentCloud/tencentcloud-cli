**Example 1: 列出访问密钥**



Input: 

```
tccli cam ListAccessKeys --cli-unfold-argument  \
    --TargetUin 123456
```

Output: 
```
{
    "Response": {
        "AccessKeys": [
            {
                "AccessKeyId": "AKIDlOp****mQsJQWEaYK",
                "Status": "Active",
                "CreateTime": "2019-12-25 14:53:03"
            },
            {
                "AccessKeyId": "A2342hOv****QOHySnzb5P7dv8",
                "Status": "Active",
                "CreateTime": "2020-03-03 16:51:21"
            }
        ],
        "RequestId": "bbc4c6b1-ee32-416a-9135-68de318c54f2"
    }
}
```

