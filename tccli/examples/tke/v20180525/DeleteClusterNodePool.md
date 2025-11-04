**Example 1: 删除节点池**

删除节点池

Input: 

```
tccli tke DeleteClusterNodePool --cli-unfold-argument  \
    --ClusterId cls-7tz3n309 \
    --NodePoolIds np-e55paxnt \
    --KeepInstance False
```

Output: 
```
{
    "Response": {
        "RequestId": "ebc80be1-c6a7-4c1f-870e-74eba8471969"
    }
}
```

