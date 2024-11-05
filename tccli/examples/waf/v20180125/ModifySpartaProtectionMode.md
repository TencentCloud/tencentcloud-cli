**Example 1: newEx**



Input: 

```
tccli waf ModifySpartaProtectionMode --cli-unfold-argument  \
    --InstanceID waf_0000000002 \
    --Edition 字符串 \
    --Domain why.qcloudwaf1234.com \
    --Type 1 \
    --Mode 10
```

Output: 
```
{
    "Response": {
        "RequestId": "7b393885-aaf2-463d-a70c-4500999d7c3f"
    }
}
```

**Example 2: 设置域名防护状态**



Input: 

```
tccli waf ModifySpartaProtectionMode --cli-unfold-argument  \
    --Domain test.domain.com \
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

**Example 3: 设置域名防护状态失败的情况**



Input: 

```
tccli waf ModifySpartaProtectionMode --cli-unfold-argument  \
    --Domain test.domain.com \
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

