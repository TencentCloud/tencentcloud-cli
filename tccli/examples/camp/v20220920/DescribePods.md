**Example 1: DescribePods**

获取Pod列表

Input: 

```
tccli camp DescribePods --cli-unfold-argument  \
    --Platform abc \
    --ProjectID abc \
    --EnvironmentName abc \
    --ApplicationID abc \
    --InstanceID abc \
    --Filters.0.Name abc \
    --Filters.0.Values abc \
    --Filters.0.Op abc \
    --Filters.0.Query abc \
    --Limit 1 \
    --Offset 1 \
    --SortOptions.0.Name abc \
    --SortOptions.0.Order abc
```

Output: 
```
{
    "Response": {
        "Pods": [
            {
                "Raw": "abc",
                "UID": "abc",
                "Name": "abc",
                "ComponentName": "abc",
                "Containers": [
                    {
                        "Name": "abc",
                        "Image": "abc",
                        "Command": [
                            "abc"
                        ],
                        "Args": [
                            "abc"
                        ],
                        "WorkingDir": "abc"
                    }
                ],
                "Region": "abc",
                "ClusterID": "abc",
                "ClusterType": "abc",
                "VPC": "abc",
                "Namespace": "abc",
                "Zone": "abc",
                "IP": "abc",
                "EIP": "abc",
                "NodeName": "abc",
                "Phase": "abc",
                "State": "abc",
                "PVCs": [
                    {
                        "Name": "abc",
                        "CBS": "abc"
                    }
                ],
                "UpdateState": "abc",
                "CurrentRevision": "abc",
                "UpdateRevision": "abc",
                "WebShell": "abc",
                "CreatedAt": "2020-09-22T00:00:00+00:00",
                "IPV6": "abc"
            }
        ],
        "TotalCount": 0,
        "Filters": [
            {
                "Name": "abc",
                "Values": [
                    "abc"
                ]
            }
        ],
        "Counts": [
            {
                "Name": "abc",
                "Values": [
                    {
                        "Name": "abc"
                    }
                ]
            }
        ],
        "RequestId": "abc"
    }
}
```

