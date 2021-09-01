**Example 1: 查询Fleet的容量信息列表**



Input: 

```
tccli gse DescribeFleetCapacity --cli-unfold-argument  \
    --FleetIds fleet-qp3g3caa-ay03mhdm \
    --Offset 0 \
    --Limit 10
```

Output: 
```
{
    "Response": {
        "FleetCapacity": [
            {
                "FleetId": "fleet-qp3g3caa-19tzbzao",
                "ScalingInterval": 3,
                "InstanceCounts": {
                    "Active": 1,
                    "Desired": 1,
                    "Idle": 1,
                    "MaxiNum": 1,
                    "MiniNum": 0,
                    "Pending": 0,
                    "Terminating": 0
                },
                "InstanceType": "S5.SMALL2"
            }
        ],
        "RequestId": "fb8ac83f-fefa-4b5d-ba12-d1dc88785e6b",
        "TotalCount": 1
    }
}
```

