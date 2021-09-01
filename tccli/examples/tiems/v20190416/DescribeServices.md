**Example 1: 描述服务**



Input: 

```
tccli tiems DescribeServices --cli-unfold-argument  \
    --Limit 1
```

Output: 
```
{
    "Response": {
        "RequestId": "7bf9843d-9153-4647-99a0-05c70ba47603",
        "Services": [
            {
                "Id": "ank95gbm4dwfhmds",
                "Cluster": "ap-beijing",
                "Region": "ap-beijing",
                "Name": "test",
                "Runtime": "pmml",
                "ModelUri": "cos://ti-ems-125502019.cos.ap-beijing.myqcloud.com/models/pmml/",
                "Cpu": 100,
                "Memory": 100,
                "Gpu": 0,
                "GpuMemory": 0,
                "CreateTime": "2019-11-07T15:14:19+08:00",
                "UpdateTime": "2019-11-07T15:14:19+08:00",
                "ScaleMode": "MANUAL",
                "Scaler": {
                    "MaxReplicas": 2,
                    "MinReplicas": 0,
                    "StartReplicas": 2,
                    "HpaMetrics": []
                },
                "Status": {
                    "DesiredReplicas": 2,
                    "CurrentReplicas": 2,
                    "Replicas": [
                        "ank95gbm4dwfhmds-fccc99cdd-ftff5",
                        "ank95gbm4dwfhmds-fccc99cdd-fvskl"
                    ],
                    "Status": "Normal",
                    "Message": "",
                    "Conditions": []
                },
                "AccessToken": "",
                "ConfigName": "test1",
                "ConfigVersion": "1.0",
                "ServeSeconds": 470,
                "ConfigId": "asjcqn7wtdgrd7gt",
                "ResourceGroupId": "ap-beijing",
                "ResourceGroupName": "公共资源组",
                "Exposes": [],
                "Description": "test",
                "GpuType": ""
            }
        ],
        "TotalCount": 2
    }
}
```

