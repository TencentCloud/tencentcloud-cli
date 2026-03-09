**Example 1: DescribeEtcdInstances**



Input: 

```
tccli cetcd DescribeEtcdInstances --cli-unfold-argument  \
    --InstanceIds etcd-abcd1234
```

Output: 
```
{
    "Response": {
        "Etcds": [
            {
                "InstanceId": "abc",
                "Name": "abc",
                "Description": "abc",
                "VpcId": "abc",
                "Version": "abc",
                "Status": "abc",
                "Members": [
                    {
                        "Name": "abc",
                        "Version": "abc",
                        "Zone": "abc",
                        "Status": "abc"
                    }
                ],
                "Endpoint": "abc",
                "DeletionProtection": true
            }
        ],
        "TotalCount": 1,
        "RequestId": "abc"
    }
}
```

