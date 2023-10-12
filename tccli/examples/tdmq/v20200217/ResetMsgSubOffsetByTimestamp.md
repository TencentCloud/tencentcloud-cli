**Example 1: 回溯消息**

{
  "EnvironmentId": "abc",
  "TopicName": "abc",
  "Subscription": "abc",
  "ToTimestamp": 1,
  "ClusterId": "abc"
}

Input: 

```
tccli tdmq ResetMsgSubOffsetByTimestamp --cli-unfold-argument  \
    --EnvironmentId abc \
    --TopicName abc \
    --Subscription abc \
    --ToTimestamp 1 \
    --ClusterId abc
```

Output: 
```
{
    "Response": {
        "Result": true,
        "RequestId": "3593f784-fcfb-4f23-b3dd-4751cba3aec7"
    }
}
```

