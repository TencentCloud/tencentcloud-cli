**Example 1: Sending custom alarm notifications**

This example shows you how to send custom alarm notifications.

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

