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
        "TotalCount": 0,
        "UsedDetailSet": [
            {
                "TrafficPackageId": "abc",
                "TrafficPackageName": "abc",
                "TotalAmount": {
                    "Value": 1,
                    "FormatValue": 0,
                    "FormatUnit": "abc"
                },
                "Deduction": {
                    "Value": 1,
                    "FormatValue": 0,
                    "FormatUnit": "abc"
                },
                "RemainingAmount": {
                    "Value": 1,
                    "FormatValue": 0,
                    "FormatUnit": "abc"
                },
                "Time": "2020-09-22 00:00:00",
                "ResourceType": "abc",
                "ResourceId": "abc",
                "ResourceName": "abc",
                "Deadline": "2020-09-22 00:00:00"
            }
        ],
        "RequestId": "abc"
    }
}
```

