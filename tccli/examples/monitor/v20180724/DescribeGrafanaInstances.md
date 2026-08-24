**Example 1: 列出 Grafana 服务**



Input: 

```
tccli monitor DescribeGrafanaInstances --cli-unfold-argument  \
    --Limit 20 \
    --Offset 0 \
    --TagFilters.0.Key tagKeyTest \
    --TagFilters.0.Value tagValueTest \
    --InstanceStatus 2 \
    --InstanceName myGrafana \
    --InstanceIds grafana-ab***fgh
```

Output: 
```
{
    "Response": {
        "InstanceSet": [
            {
                "InstanceName": "myGrafana",
                "InstanceId": "grafana-ab***fgh",
                "Region": "ap-guangzhou",
                "VpcId": "vpc-r9***9yo",
                "VpcName": "",
                "SubnetIds": [
                    "subnet-ay***78h"
                ],
                "SubnetName": "",
                "InternetUrl": "",
                "InternalUrl": "1.0.0.1:8080",
                "CreatedAt": "2020-09-22 00:00:00",
                "InstanceStatus": 0,
                "TagSpecification": [
                    {
                        "Key": "tagKeyTest",
                        "Value": "tagValueTest"
                    }
                ],
                "InstanceChargeType": 0,
                "RegionId": 1,
                "RootUrl": "https://grafana-ab***fgh.grafana.tencent-cloud.com/",
                "EnableSSO": true,
                "EnableSSOCamCheck": true,
                "Zone": "",
                "Version": "v11.6.3"
            }
        ],
        "TotalCount": 1,
        "Instances": [
            {
                "InstanceName": "myGrafana",
                "InstanceId": "grafana-ab***fgh",
                "Region": "ap-guangzhou",
                "VpcId": "vpc-r9***9yo",
                "VpcName": "",
                "SubnetIds": [
                    "subnet-ay***78h"
                ],
                "SubnetName": "",
                "InternetUrl": "",
                "InternalUrl": "1.0.0.1:8080",
                "CreatedAt": "2020-09-22 00:00:00",
                "InstanceStatus": 0,
                "TagSpecification": [
                    {
                        "Key": "tagKeyTest",
                        "Value": "tagValueTest"
                    }
                ],
                "InstanceChargeType": 0,
                "RegionId": 1,
                "RootUrl": "https://grafana-ab***fgh.grafana.tencent-cloud.com/",
                "EnableSSO": true,
                "EnableSSOCamCheck": true,
                "Zone": "",
                "Version": "v11.6.3"
            }
        ],
        "RequestId": "18cff5ac-9110-4512-abe2-5459804c9c35"
    }
}
```

