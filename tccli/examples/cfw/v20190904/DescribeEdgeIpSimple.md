**Example 1: 互联网边界开关查询**



Input: 

```
tccli cfw DescribeEdgeIpSimple --cli-unfold-argument  \
    --Filters.0.Name InstanceId \
    --Filters.0.OperatorType 9 \
    --Filters.0.Values ins-ighogubo \
    --Limit 10 \
    --Offset 0 \
    --Order PublicIp \
    --By desc
```

Output: 
```
{
    "Response": {
        "Data": [
            {
                "AssetType": "CVM",
                "InstanceId": "ins-ighogubo",
                "InstanceName": "test123",
                "PublicIp": "124.156.218.153",
                "PublicIpType": 1,
                "Region": "ap-tokyo",
                "Status": 1,
                "SwitchMode": 0
            }
        ],
        "Total": 1,
        "RequestId": "1e6399f6-58d7-4b23-b047-c94462740360"
    }
}
```

