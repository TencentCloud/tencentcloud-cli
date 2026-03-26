**Example 1: 请求示例**



Input: 

```
tccli redis DescribeLogInstanceList --cli-unfold-argument  \
    --LogType auditLog \
    --Limit 100 \
    --Offset 0
```

Output: 
```
{
    "Response": {
        "Items": [
            {
                "CreateAt": "",
                "Deliver": "",
                "DeliverSummary": null,
                "EnableQuery": "",
                "HighLogExpireDay": 0,
                "HighStorage": 0,
                "InstanceId": "crs-d285tydf",
                "InstanceInfo": {
                    "DegradeStrategy": 500,
                    "InstanceName": "test-redis-5.0-cluster-1s1r-2g",
                    "InstanceTags": [],
                    "ProjectId": 0,
                    "Region": "ap-guangzhou",
                    "Status": 2,
                    "SubStatus": 19,
                    "Type": 9,
                    "Zone": "ap-guangzhou-2"
                },
                "LogExpireDay": 0,
                "LogStorage": 0,
                "LowLogExpireDay": 0,
                "LowStorage": 0,
                "Status": ""
            }
        ],
        "TotalCount": 3,
        "RequestId": "63a0297c-850a-40df-a897-939ec135438b"
    }
}
```

