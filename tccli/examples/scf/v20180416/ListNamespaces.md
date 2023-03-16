**Example 1: 列出命名空间列表**

列出命名空间列表

Input: 

```
tccli scf ListNamespaces --cli-unfold-argument  \
    --SearchKey.0.Key Namespace \
    --SearchKey.0.Value dev
```

Output: 
```
{
    "Response": {
        "Namespaces": [
            {
                "ModTime": "2020-09-22 00:00:00",
                "AddTime": "2020-09-22 00:00:00",
                "Description": "abc",
                "Name": "abc",
                "Type": "abc",
                "Status": "abc",
                "StatusReason": "abc",
                "ResourceEnv": {
                    "TKE": {
                        "ClusterID": "abc",
                        "SubnetID": "abc",
                        "Namespace": "abc",
                        "DataPath": "abc",
                        "NodeSelector": [
                            {
                                "Key": "abc",
                                "Value": "abc"
                            }
                        ],
                        "Tolerations": [
                            {
                                "Key": "abc",
                                "Operator": "abc",
                                "Effect": "abc",
                                "Value": "abc",
                                "TolerationSeconds": 1
                            }
                        ],
                        "Port": 1
                    }
                },
                "Stamp": [
                    "abc"
                ]
            }
        ],
        "TotalCount": 0,
        "RequestId": "abc"
    }
}
```

