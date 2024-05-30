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
                "InstanceName": "abc",
                "InstanceId": "abc",
                "Region": "abc",
                "VpcId": "abc",
                "SubnetIds": [
                    "abc"
                ],
                "InternetUrl": "abc",
                "InternalUrl": "abc",
                "CreatedAt": "2020-09-22 00:00:00",
                "InstanceStatus": 0,
                "TagSpecification": [
                    {
                        "Key": "abc",
                        "Value": "abc"
                    }
                ],
                "Zone": "abc",
                "InstanceChargeType": 0,
                "VpcName": "abc",
                "SubnetName": "abc",
                "RegionId": 0,
                "RootUrl": "abc",
                "EnableSSO": true,
                "Version": "abc",
                "EnableSSOCamCheck": true
            }
        ],
        "TotalCount": 0,
        "Instances": [
            {
                "InstanceName": "abc",
                "InstanceId": "abc",
                "Region": "abc",
                "VpcId": "abc",
                "SubnetIds": [
                    "abc"
                ],
                "InternetUrl": "abc",
                "InternalUrl": "abc",
                "CreatedAt": "2020-09-22 00:00:00",
                "InstanceStatus": 0,
                "TagSpecification": [
                    {
                        "Key": "abc",
                        "Value": "abc"
                    }
                ],
                "Zone": "abc",
                "InstanceChargeType": 0,
                "VpcName": "abc",
                "SubnetName": "abc",
                "RegionId": 0,
                "RootUrl": "abc",
                "EnableSSO": true,
                "Version": "abc",
                "EnableSSOCamCheck": true
            }
        ],
        "RequestId": "abc"
    }
}
```

