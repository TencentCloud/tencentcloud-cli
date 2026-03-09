**Example 1: 查看etcd快照列表**



Input: 

```
tccli cetcd DescribeEtcdSnapshots --cli-unfold-argument  \
    --InstanceId etcd-abcd1234
```

Output: 
```
{
    "Response": {
        "RequestId": "13b59a2d-dd68-48ab-845e-8cba577eca6d",
        "Snapshots": [
            {
                "Name": "test"
            }
        ]
    }
}
```

