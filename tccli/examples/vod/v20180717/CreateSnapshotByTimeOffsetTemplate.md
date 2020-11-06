**Example 1: 创建指定时间点截图模板**



Input: 

```
tccli vod CreateSnapshotByTimeOffsetTemplate --cli-unfold-argument  \
    --Name 指定时间点截图模板1 \
    --Width 540 \
    --Height 960 \
    --Format jpg
```

Output: 
```
{
    "Response": {
        "Definition": 1008,
        "RequestId": "12ae8d8e-dce3-4151-9d4b-5594145287e1"
    }
}
```

