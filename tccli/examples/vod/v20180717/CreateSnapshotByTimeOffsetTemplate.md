**Example 1: Creating a time point screencapturing template**



Input: 

```
tccli vod CreateSnapshotByTimeOffsetTemplate --cli-unfold-argument  \
    --Name 'Time point screencapturing template 1'\
    --Width 540\
    --Height 960\
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

