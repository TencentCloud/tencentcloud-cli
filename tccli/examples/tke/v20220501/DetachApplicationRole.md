**Example 1: 指定 CVM 实例 ID 解绑**



Input: 

```
tccli tke DetachApplicationRole --cli-unfold-argument  \
    --Instances ins-fsssanl0
```

Output: 
```
{
    "Response": {
        "RequestId": "12dc6ea6-67da-4c1a-8474-1d6f57ebcf19"
    }
}
```

**Example 2: 指定集群 ID 和原生节点的 Machine ID 解绑**



Input: 

```
tccli tke DetachApplicationRole --cli-unfold-argument  \
    --ClusterId cls-bk5u1nry
```

Output: 
```
{
    "Response": {
        "RequestId": "28683e81-c659-401e-a7a6-542b6bf00b1b"
    }
}
```

