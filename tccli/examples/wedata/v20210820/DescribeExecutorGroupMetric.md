**Example 1: test**



Input: 

```
tccli wedata DescribeExecutorGroupMetric --cli-unfold-argument  \
    --TrendStartTime 1 \
    --TrendEndTime 1 \
    --ExecutorGroupId 20220426145215957124
```

Output: 
```
{
    "Response": {
        "RequestId": "8552e3a0-69ec-4c21-a4b7-142f4b9c4678",
        "Data": {
            "ExecutorGroupId": "20221208174634944660",
            "ExecutorGroupName": "资源组-dlc",
            "ExecutorGroupDesc": null,
            "RegionId": 8,
            "Region": "北京",
            "RegionEn": "ap-beijing",
            "VpcId": "vpc-87y7jn70",
            "SubnetId": "subnet-677xoxsl",
            "ProjectId": "1475268929806635008",
            "ProjectName": null,
            "ProjectDisplayName": "DLC_test"
        }
    }
}
```

