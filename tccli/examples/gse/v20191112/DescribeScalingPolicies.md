**Example 1: 查询Fleet的扩缩容配置**



Input: 

```
tccli gse DescribeScalingPolicies --cli-unfold-argument  \
    --FleetId fleet-qp3g3caa-ay03mhdm \
    --Offset 0 \
    --Limit 10
```

Output: 
```
{
    "Response": {
        "RequestId": "ed36d5af-7db8-4bd8-9c4d-ee33c0ca330d",
        "ScalingPolicies": [
            {
                "ComparisonOperator": "",
                "EvaluationPeriods": "",
                "FleetId": "fleet-qp3g3caa-19tzbzao",
                "MetricName": "",
                "Name": "",
                "PolicyType": "",
                "ScalingAdjustment": "",
                "ScalingAdjustmentType": "",
                "Status": "",
                "TargetConfiguration": {
                    "TargetValue": 30
                },
                "Threshold": ""
            }
        ],
        "TotalCount": 1
    }
}
```

