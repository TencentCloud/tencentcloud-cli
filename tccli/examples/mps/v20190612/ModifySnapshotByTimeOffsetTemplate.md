**Example 1: 修改指定时间点截图模板**



Input: 

```
tccli mps ModifySnapshotByTimeOffsetTemplate --cli-unfold-argument  \
    --Definition 10001 \
    --Format jpg \
    --Height 960 \
    --Name 指定时间点截图模板1 \
    --Width 540
```

Output: 
```
{
    "Response": {
        "RequestId": "12ae8d8e-dce3-4151-9d4b-5594145287e1"
    }
}
```

