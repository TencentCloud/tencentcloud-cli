**Example 1: 查询分散置放群组信息**

查询分散置放群组信息

Input: 

```
tccli cvm DescribeDisasterRecoverGroups --cli-unfold-argument  \
    --Offset 0 \
    --Limit 100 \
    --Filters.0.Name tag:myTagKey \
    --Filters.0.Values myTagVlue
```

Output: 
```
{
    "Response": {
        "DisasterRecoverGroupSet": [
            {
                "Affinity": 1,
                "CreateTime": "2024-08-28T10:04:56Z",
                "CurrentNum": 0,
                "CvmQuotaTotal": 60,
                "DisasterRecoverGroupId": "ps-0f03mwkn",
                "InstanceIds": [],
                "Name": "HostDisasterRecoverGroup",
                "Tags": [
                    {
                        "Key": "myTagKey",
                        "Value": "myTagVlue"
                    }
                ],
                "Type": "HOST"
            },
            {
                "Affinity": 1,
                "CreateTime": "2024-08-13T04:16:19Z",
                "CurrentNum": 0,
                "CvmQuotaTotal": 20,
                "DisasterRecoverGroupId": "ps-ali72vwj",
                "InstanceIds": [],
                "Name": "SWDisasterRecoverGroup",
                "Tags": [
                    {
                        "Key": "myTagKey",
                        "Value": "myTagVlue"
                    }
                ],
                "Type": "SW"
            }
        ],
        "RequestId": "52eca90d-08c8-4887-abf0-78d8155cfcfd",
        "TotalCount": 2
    }
}
```

