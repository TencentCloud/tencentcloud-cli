**Example 1: 成功情况的返回**



Input: 

```
tccli cos UpdateUinStat --cli-unfold-argument  \
    --AppName 23 \
    --Payload.UinId 700001107506 \
    --Payload.OpType forbid \
    --Payload.OpReason we \
    --Payload.OpUin 0 \
    --Payload.RtxUser comp \
    --Payload.Source comp
```

Output: 
```
{
    "Response": {
        "Data": 1,
        "RequestId": "162c6a69-894e-4898-962c-eff457529a5e"
    }
}
```

