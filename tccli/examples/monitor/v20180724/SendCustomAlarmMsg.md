**Example 1: 发送自定义消息告警**

发送自定义消息告警

Input: 

```
tccli monitor SendCustomAlarmMsg --cli-unfold-argument  \
    --Module monitor \
    --PolicyId cm-04rhwvwg \
    --Msg XXXX
```

Output: 
```
{
    "Response": {
        "RequestId": "9q1zxtmzw6xqyqriu8run9jf6fnnkdbn"
    }
}
```

