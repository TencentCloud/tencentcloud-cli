**Example 1: 示例1**



Input: 

```
tccli csip ModifyNotifySetting --cli-unfold-argument  \
    --Module AkSk \
    --Mode 0 \
    --Status 1 \
    --BeginTime 09:00:00 \
    --EndTime 18:00:00 \
    --Option CRITICAL
```

Output: 
```
{
    "Response": {
        "RequestId": "caaa7927-5161-4511-973f-971189e8dbdb"
    }
}
```

