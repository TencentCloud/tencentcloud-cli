**Example 1: 查看Pod列表**

查看Pod列表

Input: 

```
tccli camp DescribePods --cli-unfold-argument  \
    --ProjectID prj-27np9q4t \
    --ApplicationID app-wchnr4pv \
    --InstanceID ins-xxxx
```

Output: 
```
{
    "Response": {
        "Pods": [
            {
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
                "Zone": "abc",
                "IP": "abc",
                "Phase": "abc",
                "State": "abc",
                "CreatedAt": "2020-09-22T00:00:00+00:00",
                "UID": "abc",
                "Status": {},
                "PVCs": [
                    {
                        "Name": "abc",
                        "CBS": "abc"
                    }
                ]
            }
        ],
        "TotalCount": 0,
        "RequestId": "abc"
    }
}
```

