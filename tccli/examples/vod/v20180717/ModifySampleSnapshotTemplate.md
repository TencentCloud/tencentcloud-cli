**Example 1: 修改采样截图模板**



Input: 

```
tccli vod ModifySampleSnapshotTemplate --cli-unfold-argument  \
    --Definition 10001 \
    --Name 采样截图模板1 \
    --Width 540 \
    --Height 960 \
    --SampleType Percent \
    --SampleInterval 10 \
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

