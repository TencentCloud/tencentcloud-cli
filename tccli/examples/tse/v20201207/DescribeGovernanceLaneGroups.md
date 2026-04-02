**Example 1: 查询泳道组列表**

查询泳道组列表

Input: 

```
tccli tse DescribeGovernanceLaneGroups --cli-unfold-argument  \
    --InstanceId ins-f72d4820 \
    --Offset 1 \
    --Limit 1
```

Output: 
```
{
    "Response": {
        "LaneGroups": [
            {
                "CreateTime": "2026-01-13 18:04:50",
                "Destinations": [
                    {
                        "Namespace": "default",
                        "Service": "LaneCallerService"
                    }
                ],
                "ID": "db33e953bfd7467abe34f40f23ca1ada",
                "ModifyTime": "2026-01-15 11:43:21",
                "Name": "sct",
                "Revision": "4d6b31038976413b999b1c3117875b6d",
                "Rules": [
                    {
                        "CreateTime": "2026-01-14 11:23:47",
                        "Description": "blue",
                        "Enable": true,
                        "EnableTime": "2026-01-15 11:41:17",
                        "ID": "15d28168fe894299b50d49b35193867c",
                        "LaneGroup": "sct",
                        "LaneLabelValue": "blue",
                        "LaneMatchMode": "PERMISSIVE",
                        "ModifyTime": "2026-01-15 11:43:21",
                        "Name": "blue",
                        "Priority": 0,
                        "Revision": "a023fd6b2f1441158699177ad3a86213",
                        "TrafficGray": {
                            "Curvature": 0,
                            "IntervalSecond": 0,
                            "Mode": "PERCENTAGE",
                            "Percent": 100
                        },
                        "TrafficLabels": [
                            {
                                "Key": "color",
                                "Type": "HEADER",
                                "Value": {
                                    "Type": "EXACT",
                                    "Value": "blue",
                                    "ValueType": "TEXT"
                                }
                            }
                        ],
                        "TrafficMatchMode": "AND"
                    }
                ],
                "TrafficEntries": [
                    {
                        "EntryType": "polarismesh.cn/gateway/spring-cloud-gateway",
                        "ServiceGatewaySelector": {
                            "Namespace": "default",
                            "Service": "LaneRouterGatewayService"
                        }
                    }
                ]
            }
        ],
        "Total": 3,
        "RequestId": "de77ec4e-e69f-459e-9c07-13b32b207bcc"
    }
}
```

