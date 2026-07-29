**Example 1: 查询集群中的节点配置**

已经加入到集群中的节点独特属性信息查看

Input: 

```
tccli dbdc DescribeDBCustomClusterNodeConfig --cli-unfold-argument  \
    --ClusterId dbcc-sizxd0hi \
    --NodeIds dbcn-7d59rhi5
```

Output: 
```
{
    "Response": {
        "NodeSet": [
            {
                "Labels": [
                    {
                        "Key": "tke.cloud.tencent.com/cbs-mountable",
                        "Value": "true"
                    }
                ],
                "NodeId": "dbcn-7d59rhi5",
                "Taints": []
            }
        ],
        "RequestId": "013a1d89-8fc3-408b-bf28-b43fb7e62ff2"
    }
}
```

