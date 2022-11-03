**Example 1: 修改采样截图模板**



Input: 

```
tccli mps ModifySampleSnapshotTemplate --cli-unfold-argument  \
    --Definition 10001 \
    --Name 采样截图模板1 \
    --Format jpg \
    --SampleType Percent \
    --Height 960 \
    --Width 540 \
    --SampleInterval 10
```

Output: 
```
{
    "Response": {
        "RequestId": "12ae8d8e-dce3-4151-9d4b-5594145287e1"
    }
}
```

