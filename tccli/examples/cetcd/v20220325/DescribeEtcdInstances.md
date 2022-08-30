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
                "Description": "第一版测试",
                "Endpoint": "",
                "InstanceId": "etcd-abcd1234",
                "Members": null,
                "Name": "etcd-test-cluster",
                "Status": "running",
                "Version": "v3.3.11",
                "VpcId": "vpc-abcd1234"
            }
        ],
        "RequestId": "51abd77d-f503-41e7-ab28-010083e02a78",
        "TotalCount": 1
    }
}
```

