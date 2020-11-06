**Example 1: SendOnlineMsg**



Input: 

```
tccli iotvideo SendOnlineMsg --cli-unfold-argument  \
    --Tid 031400005e005a3838bd481dbe61db28 \
    --Wakeup true \
    --WaitResp 2 \
    --MsgTopic test \
    --MsgContent {"test":"test"}
```

Output: 
```
{
    "Response": {
        "RequestId": "af1f328c-5856-4719-b86e-b31420dfc3d6",
        "TaskId": "",
        "Data": "{\"test\":\"test\"}"
    }
}
```

