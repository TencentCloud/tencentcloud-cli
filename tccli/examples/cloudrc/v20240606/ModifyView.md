**Example 1: 修改视图**



Input: 

```
tccli cloudrc ModifyView --cli-unfold-argument  \
    --ViewId vw-vr1yfbg7 \
    --ViewName 测试视图 \
    --Filters.0.Values ap-guangzhou
```

Output: 
```
{
    "Response": {
        "RequestId": "4d9ed385-e0cc-4733-bf5e-cd3f2669d3f7"
    }
}
```

