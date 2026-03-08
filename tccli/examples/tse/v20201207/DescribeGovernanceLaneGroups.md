**Example 1: 查询泳道组列表**

查询泳道组列表

Input: 

```
tccli tse DescribeGovernanceLaneGroups --cli-unfold-argument  \
    --InstanceId abc \
    --Name abc \
    --GroupID abc \
    --Offset 0 \
    --Limit 0
```

Output: 
```
{
    "Response": {
        "Total": 0,
        "LaneGroups": [
            {
                "Name": "abc",
                "ID": "abc",
                "TrafficEntries": [
                    {
                        "EntryType": "abc",
                        "TSEGatewaySelector": {
                            "GatewayId": "abc",
                            "Services": [
                                "abc"
                            ]
                        },
                        "ServiceGatewaySelector": {
                            "Namespace": "abc",
                            "Service": "abc",
                            "Labels": [
                                {
                                    "Key": "abc",
                                    "Value": "abc"
                                }
                            ]
                        },
                        "ServiceSelector": {
                            "Namespace": "abc",
                            "Service": "abc",
                            "Labels": [
                                {
                                    "Key": "abc",
                                    "Value": "abc"
                                }
                            ]
                        }
                    }
                ],
                "Destinations": [
                    {
                        "Namespace": "abc",
                        "Service": "abc",
                        "Labels": [
                            {
                                "LabelKey": "abc",
                                "LabelValue": "abc",
                                "LabelType": "abc",
                                "LabelValueType": "abc"
                            }
                        ]
                    }
                ],
                "Description": "abc",
                "Rules": [
                    {
                        "ID": "abc",
                        "Name": "abc",
                        "LaneGroup": "abc",
                        "Enable": true,
                        "TrafficLabels": [
                            {
                                "Type": "abc",
                                "Key": "abc",
                                "Value": {
                                    "Type": "abc",
                                    "Value": "abc",
                                    "ValueType": "abc"
                                }
                            }
                        ],
                        "TrafficMatchMode": "abc",
                        "LaneMatchMode": "abc",
                        "Description": "abc",
                        "LaneLabelValue": "abc",
                        "CreateTime": "abc",
                        "EnableTime": "abc",
                        "ModifyTime": "abc",
                        "Priority": 0,
                        "Revision": "abc"
                    }
                ],
                "Revision": "abc",
                "CreateTime": "abc",
                "ModifyTime": "abc",
                "Consistency": "abc"
            }
        ],
        "RequestId": "abc"
    }
}
```

