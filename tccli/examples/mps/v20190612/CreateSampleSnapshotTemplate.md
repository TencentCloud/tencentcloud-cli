**Example 1: 创建采样截图模板**



Input: 

```
tccli mps CreateSampleSnapshotTemplate --cli-unfold-argument  \
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
        "Definition": 1008,
        "RequestId": "12ae8d8e-dce3-4151-9d4b-5594145287e1"
    }
}
```

