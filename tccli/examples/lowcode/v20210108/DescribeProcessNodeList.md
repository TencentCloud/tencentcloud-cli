**Example 1: 查询流程节点信息**



Input: 

```
tccli lowcode DescribeProcessNodeList --cli-unfold-argument  \
    --ProcessVersion 0 \
    --EnvId env-001 \
    --ProcessKey xx
```

Output: 
```
{
    "Response": {
        "Data": [
            {
                "NodeId": "xx",
                "NodeName": "xx"
            }
        ],
        "RequestId": "xx"
    }
}
```

