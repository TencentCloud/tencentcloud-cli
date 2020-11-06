**Example 1: 将集群内节点移入节点池**



Input: 

```
tccli tke AddNodeToNodePool --cli-unfold-argument  \
    --ClusterId cls-xxxxxx \
    --NodePoolId np-xxxxxx \
    --InstanceIds ins-xxx
```

Output: 
```
{
    "Response": {
        "RequestId": "xxxx"
    }
}
```

