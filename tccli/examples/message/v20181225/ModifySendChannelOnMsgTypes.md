**Example 1: 批量修改消息接收渠道**



Input: 

```
tccli message ModifySendChannelOnMsgTypes --cli-unfold-argument  \
    --SendTypes.0.MsgType 207 \
    --SendTypes.0.SendChannel 7
```

Output: 
```
{
    "Response": {
        "RequestId": "85d1906b-274b-44ac-a22e-4fdc00822347"
    }
}
```

