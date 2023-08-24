**Example 1: 设置域名防护状态**



Input: 

```
tccli waf ModifySpartaProtectionMode --cli-unfold-argument  \
    --Domain xx \
    --Mode 21 \
    --Edition sparta-waf
```

Output: 
```
{
    "Response": {
        "RequestId": "225e3456-c296-475d-9338-b055667e6c85"
    }
}
```

**Example 2: 设置域名防护状态失败的情况**



Input: 

```
tccli waf ModifySpartaProtectionMode --cli-unfold-argument  \
    --Domain xx \
    --Mode 21 \
    --Edition sparta-waf
```

Output: 
```
{
    "Response": {
        "Error": {
            "Code": "InternalError",
            "Message": "非法的模式"
        },
        "RequestId": "8bc47086-2922-4bfb-b154-db325abc1a28"
    }
}
```

