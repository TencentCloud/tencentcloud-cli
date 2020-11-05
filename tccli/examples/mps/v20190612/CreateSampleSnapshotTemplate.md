**Example 1: Creating a sampled screencapturing template**



Input: 

```
tccli mps CreateSampleSnapshotTemplate --cli-unfold-argument  \
    --Name 'Sampled screencapturing template 1'\
    --Width 540\
    --Height 960\
    --SampleType Percent\
    --SampleInterval 10\
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

