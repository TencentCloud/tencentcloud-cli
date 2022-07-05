**Example 1: 获取边缘脚本链接**



Input: 

```
tccli tke DescribeTKEEdgeScript --cli-unfold-argument  \
    --Interface eth0 \
    --Config {} \
    --ClusterId cls123 \
    --NodeName node
```

Output: 
```
{
    "Response": {
        "Link": "www.tencent.com",
        "Token": "123456",
        "Command": "wget www.tencent.com",
        "RequestId": "eac6b301-a322-493a-8e36-83b295459397"
    }
}
```

