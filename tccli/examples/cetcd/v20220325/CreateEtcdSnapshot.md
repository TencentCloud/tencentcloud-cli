**Example 1: 创建etcd快照**



Input: 

```
tccli cetcd CreateEtcdSnapshot --cli-unfold-argument  \
    --InstanceId etcd-abcd1345 \
    --SnapshotName test \
    --User test \
    --Password 123
```

Output: 
```
{
    "Response": {
        "RequestId": "13b59a2d-dd68-48ab-845e-8cba577eca6d"
    }
}
```

