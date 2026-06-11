**Example 1: 创建集群的周期弹性策略**



Input: 

```
tccli cynosdb CreateClusterPeriodScalePolicy --cli-unfold-argument  \
    --ClusterId cynosdbmysql-xdbsbsgg \
    --InstanceType rw \
    --ScaleStartTime 10:00 \
    --ScaleEndTime 14:00 \
    --PolicyStartTime 2025-10-01 00:00:00 \
    --PolicyEndTime 2025-12-01 00:00:00 \
    --PeriodType day \
    --MinCpu 0.5 \
    --MaxCpu 2
```

Output: 
```
{
    "Response": {
        "PolicyId": "cynosdbmysql-spd-rye0gd5b",
        "RequestId": "3c140219-cfe9-470e-b241-907877d6fb03"
    }
}
```

