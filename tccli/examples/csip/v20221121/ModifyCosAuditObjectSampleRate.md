**Example 1: 修改COS审计采样率**



Input: 

```
tccli csip ModifyCosAuditObjectSampleRate --cli-unfold-argument  \
    --BucketIdSet 1346438 \
    --SampleRateSet 0.5 \
    --TargetAppId 260209268 \
    --DefaultSampleRate 0.01
```

Output: 
```
{
    "Response": {
        "DefaultSampleRate": 0.01,
        "DefaultSampleRateUpdated": true,
        "RequestId": "466d34ac-169a-4b5e-b194-9541b0871a66",
        "UpdatedBucketCount": 1
    }
}
```

