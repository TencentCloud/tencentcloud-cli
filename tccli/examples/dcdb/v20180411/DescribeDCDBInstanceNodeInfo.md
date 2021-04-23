**Example 1: 获取实例节点信息**



Input: 

```
tccli dcdb DescribeDCDBInstanceNodeInfo --cli-unfold-argument  \
    --InstanceId tdsqlshard-8upuqubt
```

Output: 
```
{
    "Response": {
        "NodesInfo": [
            {
                "NodeId": "b991a3d602da35cf7bf64dcafcd5f7ad589aa6d9",
                "Role": "master",
                "ShardId": "shard-he2hj3al"
            },
            {
                "NodeId": "9a498278e1775355cac16c23d65c59204aec52f1",
                "Role": "slave",
                "ShardId": "shard-he2hj3al"
            },
            {
                "NodeId": "3c698ab9547674e361bae013439225356175668d",
                "Role": "master",
                "ShardId": "shard-mgsnag2z"
            },
            {
                "NodeId": "2f0714ded5eaef1dd927fdc1429350470ce0017b",
                "Role": "slave",
                "ShardId": "shard-mgsnag2z"
            }
        ],
        "RequestId": "6b8b1984-c226-46d9-ac0a-81e241cf7cdc",
        "TotalCount": 4
    }
}
```

