**Example 1: 新建作品**

新建作品

Input: 

```
tccli bma CreateCRWork --cli-unfold-argument  \
    --WhiteLists xx \
    --IsMonitor xx \
    --MonitorUrl xx \
    --IsOriginal xx \
    --SampleDownloadURL xx \
    --ProducerID 0 \
    --IsRelease xx \
    --WorkCategory xx \
    --WorkDesc xx \
    --WorkName xx \
    --SamplePublicURL xx \
    --ProduceTime xx \
    --CertUrl xx \
    --ProduceType xx \
    --IsCert xx \
    --SampleContentURL xx \
    --GrantType xx \
    --WorkSign xx \
    --WorkPic xx \
    --WorkType xx \
    --ProducerName xx
```

Output: 
```
{
    "Response": {
        "EvidenceId": 0,
        "RequestId": "xx",
        "WorkId": 0
    }
}
```

