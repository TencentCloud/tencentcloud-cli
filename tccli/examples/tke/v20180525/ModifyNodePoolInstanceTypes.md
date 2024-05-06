**Example 1: 修改节点池机型**

修改节点池机型

Input: 

```
tccli tke ModifyNodePoolInstanceTypes --cli-unfold-argument  \
    --ClusterId cls-xxx \
    --InstanceTypes ins-xxx \
    --NodePoolId np-xxx
```

Output: 
```
{
    "Response": {
        "RequestId": "xxxxxxxx"
    }
}
```

