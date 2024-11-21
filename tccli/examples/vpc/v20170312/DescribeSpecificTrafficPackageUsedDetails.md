**Example 1: 查询某个流量包的用量明细**

查询某个流量包的用量明细。

Input: 

```
tccli vpc DescribeSpecificTrafficPackageUsedDetails --cli-unfold-argument  \
    --TrafficPackageId tfp-f7a3qh6x
```

Output: 
```
{
    "Response": {
        "TotalCount": 1,
        "UsedDetailSet": [
            {
                "TrafficPackageId": "tfp-f7a3qh6x",
                "TrafficPackageName": "demo",
                "TotalAmount": {
                    "Value": 3298534883328,
                    "FormatValue": 3,
                    "FormatUnit": "TB"
                },
                "Deduction": {
                    "Value": 6562480603,
                    "FormatValue": 6.1118,
                    "FormatUnit": "GB"
                },
                "RemainingAmount": {
                    "Value": 2923154413867,
                    "FormatValue": 2.6586,
                    "FormatUnit": "TB"
                },
                "Time": "2020-09-22 00:00:00",
                "ResourceType": "CVM",
                "ResourceId": "ins-izj1qrhj",
                "ResourceName": "demo",
                "Deadline": "2020-09-22 00:00:00"
            }
        ],
        "RequestId": "9fd8594c-53ae-4439-8054-db97b9580bea"
    }
}
```

