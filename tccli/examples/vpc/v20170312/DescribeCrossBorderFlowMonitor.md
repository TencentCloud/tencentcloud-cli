**Example 1: 查询跨境带宽监控数据**

查询跨境带宽监控数据

Input: 

```
tccli vpc DescribeCrossBorderFlowMonitor --cli-unfold-argument  \
    --CcnId ccn-gree226l \
    --CcnUin 251223380 \
    --SourceRegion ap-guangzhou \
    --DestinationRegion ap-shanghai \
    --Period 60 \
    --StartTime 2022-08-20 00:00:00 \
    --EndTime 2022-08-20 00:10:00
```

Output: 
```
{
    "Response": {
        "CrossBorderFlowMonitorData": [
            {
                "InBandwidth": [
                    1,
                    1
                ],
                "InPkg": [
                    1,
                    2
                ],
                "OutBandwidth": [
                    1,
                    3
                ],
                "OutPkg": [
                    1,
                    4
                ]
            }
        ],
        "RequestId": "ff8a76ff-8900-4169-b126-ff59fdb39b6c"
    }
}
```

