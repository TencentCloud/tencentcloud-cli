**Example 1: 获取边缘脚本链接**



Input: 

```
tccli tke DescribeTKEEdgeScript --cli-unfold-argument  \
    --ClusterId cls123 \
    --NodeName node \
    --Interface eth0 \
    --Config {}
```

Output: 
```
{
    "Response": {
        "RequestId": "eac6b301-a322-493a-8e36-83b295459397"
    }
}
```

