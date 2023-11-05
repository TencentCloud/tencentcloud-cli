**Example 1: VPC防火墙(组)开关列表**



Input: 

```
tccli ocfw DescribeVpcFwGroupSwitch --cli-unfold-argument  \
    --Filters.0.Name abc \
    --Filters.0.Values abc \
    --Filters.0.OperatorType 0 \
    --Limit 1 \
    --Offset 1 \
    --StartTime abc \
    --EndTime abc \
    --Order abc \
    --By abc \
    --CurrentAppId 1
```

Output: 
```
{
    "Response": {
        "SwitchList": [
            {
                "SwitchId": "abc",
                "SwitchName": "abc",
                "SwitchMode": 0,
                "ConnectType": 0,
                "ConnectId": "abc",
                "ConnectName": "abc",
                "SrcInstancesInfo": [
                    {
                        "InstanceId": "abc",
                        "InstanceName": "abc",
                        "InstanceCidr": "abc",
                        "Region": "abc"
                    }
                ],
                "DstInstancesInfo": [
                    {
                        "InstanceId": "abc",
                        "InstanceName": "abc",
                        "InstanceCidr": "abc",
                        "Region": "abc"
                    }
                ],
                "FwGroupId": "abc",
                "FwGroupName": "abc",
                "Enable": 0,
                "Status": 0,
                "AttachWithEdge": 0,
                "CrossEdgeStatus": 0,
                "FwInsId": "abc",
                "FwInsName": "abc",
                "FwInsRegion": [
                    "abc"
                ]
            }
        ],
        "Total": 1,
        "RequestId": "abc"
    }
}
```

