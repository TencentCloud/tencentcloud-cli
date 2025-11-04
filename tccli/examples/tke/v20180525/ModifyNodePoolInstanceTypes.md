**Example 1: 修改节点池机型**

修改节点池机型

Input: 

```
tccli tke ModifyNodePoolInstanceTypes --cli-unfold-argument  \
    --ClusterId cls-e55paxnt \
    --InstanceTypes S6.MEDIUM4 S5.MEDIUM4 SA3.MEDIUM4 \
    --NodePoolId np-e55paxnt
```

Output: 
```
{
    "Response": {
        "RequestId": "d174dcb6-659b-4ab6-9533-e470a7d91e43"
    }
}
```

