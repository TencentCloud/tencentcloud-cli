**Example 1: 查询数据流动带宽**

查询数据流动带宽

Input: 

```
tccli goosefs QueryDataRepositoryBandwidth --cli-unfold-argument  \
    --FileSystemId x_c60_123456
```

Output: 
```
{
    "Response": {
        "Bandwidth": 600,
        "MinBandwidth": 0,
        "BandwidthStatus": 1,
        "RequestId": "b3caa32f-5e39-4360-91e4-5724369b78a6"
    }
}
```

