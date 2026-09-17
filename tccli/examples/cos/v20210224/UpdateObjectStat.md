**Example 1: 成功请求**



Input: 

```
tccli cos UpdateObjectStat --cli-unfold-argument  \
    --AppName costest \
    --Payload.OpType forbid \
    --Payload.OpReason 色情内容 \
    --Payload.ForbidValue 1 \
    --Payload.OpUin 0 \
    --Payload.RtxUser tarzanzhang \
    --Payload.Source cos \
    --Payload.Url http://forbid-test01-1300258161.cos.yfb.myqcloud.com/autotest/object_forbid/d2ac0e75cd234a818150e4107147b379.txt \
    --AuthTimeStamp 1781523293 \
    --AuthSign b8f2ecd8aa40ff39cf6236c9bd0fd5c48cf8fad404eb1b8556e6f145f3f2ac92
```

Output: 
```
{
    "Response": {
        "Data": 1,
        "RequestId": "1db799cc-c55c-4e3b-b080-01cd3b302622"
    }
}
```

