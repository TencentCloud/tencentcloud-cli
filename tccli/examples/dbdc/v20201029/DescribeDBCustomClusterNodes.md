**Example 1: 查询 DB Custom 集群的节点列表**



Input: 

```
tccli dbdc DescribeDBCustomClusterNodes --cli-unfold-argument  \
    --ClusterId dbcc-0cj0av3j
```

Output: 
```
{
    "Response": {
        "NodeSet": [
            {
                "LanIP": "10.0.0.1",
                "NodeId": "dbcn-0zan5xxk",
                "NodeName": "测试节点1",
                "NodeType": "DB.AT5.8XLARGE128",
                "SSHEndpoint": "10.0.0.100:36000",
                "Status": "running",
                "Zone": "ap-shanghai-5"
            }
        ],
        "TotalCount": 1,
        "RequestId": "4603723b-56f3-4466-a46b-8fe4e9348918"
    }
}
```

