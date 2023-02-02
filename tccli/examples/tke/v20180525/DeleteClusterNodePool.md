**Example 1: 删除节点池**



Input: 

```
tccli tke DeleteClusterNodePool --cli-unfold-argument  \
    --ClusterId cls-xxxxxx \
    --KeepInstance true \
    --NodePoolIds np-xxxxxxxx
```

Output: 
```
{
    "Response": {
        "RequestId": "xxxx"
    }
}
```

