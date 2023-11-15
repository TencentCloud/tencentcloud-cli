**Example 1: 删除专业集群**

删除专业集群，支持同时删除多个专业集群

Input: 

```
tccli tdmq DeleteProClusters --cli-unfold-argument  \
    --ClusterIds abc
```

Output: 
```
{
    "Response": {
        "DealNames": [
            "abc"
        ],
        "ClusterIds": [
            "abc"
        ],
        "RequestId": "abc"
    }
}
```

