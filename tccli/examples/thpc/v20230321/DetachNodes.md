**Example 1: 从集群解绑计算节点**

集群ID为hpc-2j8ntf9l的集群解绑计算节点node-8workmoi

Input: 

```
tccli thpc DetachNodes --cli-unfold-argument  \
    --ClusterId hpc-2j8ntf9l \
    --NodeIds node-8workmoi
```

Output: 
```
{
    "Response": {
        "RequestId": "40c2e07e-8500-4460-8db8-666d0e791ee5"
    }
}
```

