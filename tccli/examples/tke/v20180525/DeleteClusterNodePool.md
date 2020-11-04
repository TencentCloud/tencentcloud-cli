**Example 1: 删除节点池**



Input: 

```
tccli tke DeleteClusterNodePool --cli-unfold-argument  \
    --ClusterId cls-xxxxxx\
    --NodePoolIds np-xxxxxxxx\
    --KeepInstance true
```

Output: 
```
{
    "Response": {
        "RequestId": "xxxx"
    }
}
```

