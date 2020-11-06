**Example 1: Modifying a sampled screencapturing template**



Input: 

```
tccli vod ModifySampleSnapshotTemplate --cli-unfold-argument  \
    --Definition 10001 \
    --Name 'Sampled screencapturing template 1' \
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

