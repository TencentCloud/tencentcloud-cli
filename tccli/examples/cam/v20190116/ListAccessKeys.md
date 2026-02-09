**Example 1: 列出访问密钥**

列出访问密钥

Input: 

```
tccli cam ListAccessKeys --cli-unfold-argument  \
    --TargetUin 100013065917
```

Output: 
```
{
    "Response": {
        "AccessKeys": [
            {
                "AccessKeyId": "AKID***",
                "Status": "Active",
                "CreateTime": "2019-12-25 14:53:03"
            },
            {
                "AccessKeyId": "AKID***",
                "Status": "Active",
                "CreateTime": "2020-03-03 16:51:21"
            }
        ],
        "RequestId": "bbc4c6b1-ee32-416a-9135-68de318c54f2"
    }
}
```

