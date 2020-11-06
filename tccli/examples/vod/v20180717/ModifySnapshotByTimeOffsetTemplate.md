**Example 1: Modifying a time point screencapturing template**



Input: 

```
tccli vod ModifySnapshotByTimeOffsetTemplate --cli-unfold-argument  \
    --Definition 10001 \
    --Name 'Time point screencapturing template 1' \
    --Width 540 \
    --Height 960 \
    --Format jpg
```

Output: 
```
{
    "Response": {
        "RequestId": "12ae8d8e-dce3-4151-9d4b-5594145287e1"
    }
}
```

