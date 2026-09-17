**Example 1: 成功的下的返回**



Input: 

```
tccli cos UpdateBucketStat --cli-unfold-argument  \
    --AppName sdsfd \
    --Payload.OpType forbid \
    --Payload.OpReason dds \
    --Payload.RtxUser nedzzhang \
    --Payload.Source cos \
    --Payload.OpUin 0 \
    --Payload.Url http://forbid-test01-1300258161.cos.yfb.myqcloud.com/autotest/object_forbid/64723999a18e46998120cb35648df7ec.txt
```

Output: 
```
{
    "Response": {
        "Data": 1,
        "RequestId": "6543d4be-54ca-4bcd-985a-7ed430346fd3"
    }
}
```

