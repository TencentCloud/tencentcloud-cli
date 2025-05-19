**Example 1: 将集群内节点移入节点池**

将集群内节点移入节点池

Input: 

```
tccli tke AddNodeToNodePool --cli-unfold-argument  \
    --ClusterId cls-e55paxnt \
    --NodePoolId np-e55paxnt \
    --InstanceIds ins-e55paxnt
```

Output: 
```
{
    "Response": {
        "RequestId": "d174dcb6-659b-4ab6-9533-e470a7d91e43"
    }
}
```

