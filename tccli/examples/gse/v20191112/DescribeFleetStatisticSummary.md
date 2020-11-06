**Example 1: 查询舰队统计汇总信息**



Input: 

```
tccli gse DescribeFleetStatisticSummary --cli-unfold-argument  \
    --EndTime 2020-09-22 00:00:00 \
    --FleetId fleet-qp3g3caa-nkeekxw6 \
    --BeginTime 2020-09-22 00:00:00
```

Output: 
```
{
    "Response": {
        "TotalUsedTimeSeconds": "60",
        "TotalUsedFlowMegaBytes": "1024",
        "RequestId": "4520ba54-982e-46e2-9a0b-63c963c34fc6"
    }
}
```

