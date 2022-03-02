**Example 1: 查询实例**



Input: 

```
tccli tdcpg DescribeClusterInstances --cli-unfold-argument  \
    --ClusterId tdcpg-77iesdqa \
    --OrderBy CreateTime \
    --OrderByType DESC \
    --PageNumber 1 \
    --Filters.0.Values tdcpg-ins-6c6xs52r \
    --Filters.0.Name InstanceId \
    --Filters.0.ExactMatch True \
    --PageSize 10
```

Output: 
```
{
    "Response": {
        "InstanceSet": [
            {
                "CPU": 1,
                "ClusterId": "tdcpg-77iesdqa",
                "CreateTime": "2021-12-08T19:50:56+08:00",
                "DBVersion": "10.17",
                "EndpointId": "tdcpg-ep-6c6xs52r",
                "InstanceId": "tdcpg-ins-pzu77n6e",
                "InstanceName": "tdcpg-ins-pzu77n6e",
                "InstanceType": "RW",
                "Memory": 1,
                "PayMode": "PREPAID",
                "PayPeriodEndTime": "2022-01-08T19:50:54+08:00",
                "Region": "ap-guangzhou",
                "Status": "running",
                "StatusDesc": "运行中",
                "Zone": "ap-guangzhou-2"
            }
        ],
        "RequestId": "e0ef1b06-405f-48cc-863f-185dbb6eb037",
        "TotalCount": 1
    }
}
```

