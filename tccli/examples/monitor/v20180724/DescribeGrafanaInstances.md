**Example 1: 列出 Grafana 服务**



Input: 

```
tccli monitor DescribeGrafanaInstances --cli-unfold-argument  \
    --Limit 20 \
    --Offset 0 \
    --TagFilters.0.Key tagKeyTest \
    --TagFilters.0.Value tagValueTest \
    --InstanceStatus 2 \
    --InstanceName test \
    --InstanceIds grafana-abcdefgh
```

Output: 
```
{
    "Response": {
        "InstanceSet": [
            {
                "InstanceStatus": 0,
                "VpcId": "xx",
                "RootUrl": "xx",
                "Version": "xx",
                "Zone": "xx",
                "TagSpecification": [
                    {
                        "Value": "xx",
                        "Key": "xx"
                    }
                ],
                "InstanceId": "xx",
                "SubnetIds": [
                    "xx"
                ],
                "RegionId": 0,
                "InstanceChargeType": 0,
                "InternalUrl": "xx",
                "VpcName": "xx",
                "EnableSSOCamCheck": true,
                "SubnetName": "xx",
                "InternetUrl": "xx",
                "EnableSSO": true,
                "InstanceName": "xx",
                "Region": "xx",
                "CreatedAt": "2020-09-22 00:00:00"
            }
        ],
        "TotalCount": 1,
        "RequestId": "xx",
        "Instances": [
            {
                "InstanceStatus": 0,
                "VpcId": "xx",
                "RootUrl": "xx",
                "Version": "xx",
                "Zone": "xx",
                "TagSpecification": [
                    {
                        "Value": "xx",
                        "Key": "xx"
                    }
                ],
                "InstanceId": "xx",
                "SubnetIds": [
                    "xx"
                ],
                "RegionId": 0,
                "InstanceChargeType": 0,
                "InternalUrl": "xx",
                "VpcName": "xx",
                "EnableSSOCamCheck": true,
                "SubnetName": "xx",
                "InternetUrl": "xx",
                "EnableSSO": true,
                "InstanceName": "xx",
                "Region": "xx",
                "CreatedAt": "2020-09-22 00:00:00"
            }
        ]
    }
}
```

