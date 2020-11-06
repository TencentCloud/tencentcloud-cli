**Example 1: Creating a sampled screencapturing template (with specified width and height)**



Input: 

```
tccli vod CreateSampleSnapshotTemplate --cli-unfold-argument  \
    --Name 'Screencapturing with specified width and height' \
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
        "Definition": 1008,
        "RequestId": "12ae8d8e-dce3-4151-9d4b-5594145287e1"
    }
}
```

**Example 2: Creating a sampled screencapturing template (with specified long side)**



Input: 

```
tccli vod CreateSampleSnapshotTemplate --cli-unfold-argument  \
    --Name 'Long side screencapturing' \
    --Width 0 \
    --Height 0 \
    --Long 1080 \
    --SampleType Percent \
    --SampleInterval 10 \
    --Format jpg
```

Output: 
```
{
    "Response": {
        "Definition": 1009,
        "RequestId": "45ae8d8e-dce3-4151-9d4b-5594145287e1"
    }
}
```

