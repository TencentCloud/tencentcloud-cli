**Example 1: 查询流程节点信息**



Input: 

```
tccli lowcode DescribeProcessNodeList --cli-unfold-argument  \
    --ProcessKey abc \
    --ProcessVersion 0 \
    --EnvType abc \
    --EnvId abc
```

Output: 
```
{
    "Response": {
        "Data": [
            {
                "NodeId": "abc",
                "NodeName": "abc"
            }
        ],
        "RequestId": "abc"
    }
}
```

