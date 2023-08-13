**Example 1: 查询北极星类型的 Trait 列表**

查询北极星类型的 Trait 列表

Input: 

```
tccli camp DescribeTraits --cli-unfold-argument  \
    --ApplicationID app-sb5z5mmj \
    --ProjectID prj-d2bd4gfn \
    --InstanceID ins-xxxx \
    --Filters.0.Name Type \
    --Filters.0.Values deploy polaris \
    --Filters.1.Name ComponentName \
    --Filters.1.Values app \
    --Limit 10 \
    --Offset 0
```

Output: 
```
{
    "Response": {
        "TraitOnComponents": [
            {
                "ComponentName": "abc",
                "Trait": [
                    {
                        "Name": "abc",
                        "Type": "abc",
                        "Properties": {
                            "UpdateStrategy": {
                                "Type": "abc",
                                "MaxUnavailable": 0,
                                "MaxSurge": 0,
                                "RollingUpdate": {
                                    "Clusters": [
                                        "abc"
                                    ],
                                    "ClusterLabelSelectors": [
                                        {
                                            "MatchLabels": [
                                                {
                                                    "Key": "abc",
                                                    "Value": "abc"
                                                }
                                            ],
                                            "ReleaseOrder": 1
                                        }
                                    ],
                                    "Partition": 0
                                },
                                "BatchUpdate": {
                                    "MaxFailed": 0,
                                    "PodsToUpdate": [
                                        "abc"
                                    ]
                                },
                                "Pause": true
                            },
                            "Polaris": {
                                "Objects": [
                                    {
                                        "Name": "abc",
                                        "PolarisNamespace": "abc",
                                        "PolarisName": "abc",
                                        "Token": "abc",
                                        "CustomWeight": [
                                            "abc"
                                        ],
                                        "Weight": 0,
                                        "Ports": [
                                            {
                                                "Name": "abc",
                                                "Port": 0,
                                                "Protocol": "abc"
                                            }
                                        ],
                                        "SyncMode": "abc",
                                        "SiteZone": "abc",
                                        "TTL": "abc",
                                        "InstanceLabel": [
                                            {
                                                "Key": "abc",
                                                "Value": "abc"
                                            }
                                        ],
                                        "Selector": [
                                            {
                                                "Key": "abc",
                                                "Value": "abc"
                                            }
                                        ]
                                    }
                                ]
                            },
                            "Replicas": {
                                "Replicas": 0
                            },
                            "HPA": "abc"
                        }
                    }
                ]
            }
        ],
        "TotalCount": 1,
        "RequestId": "abc"
    }
}
```

