**Example 1: 创建直播录制模板**

创建直播录制模板

Input: 

```
tccli mps CreateLiveRecordTemplate --cli-unfold-argument  \
    --HLSConfigure.ItemDuration 10 \
    --HLSConfigure.Interval 3600 \
    --Name 模板1 \
    --Comment test
```

Output: 
```
{
    "Response": {
        "Definition": 20001,
        "RequestId": "12ae8cxc-dce3-4151-9cyt-5594145287e1"
    }
}
```

