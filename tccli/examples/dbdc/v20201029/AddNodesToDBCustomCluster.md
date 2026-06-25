**Example 1: 集群添加已有节点（通过密钥登录节点）**



Input: 

```
tccli dbdc AddNodesToDBCustomCluster --cli-unfold-argument  \
    --ClusterId dbcc-qjv7nng7 \
    --NodeIds dbcn-z4z0rbc9 \
    --ImageId img-1tmhysjj \
    --LoginSettings.KeyIds skey-48hbnu45
```

Output: 
```
{
    "Response": {
        "TaskId": 753,
        "RequestId": "96d5fa5c-44f8-48d2-88fe-81f34b71ac07"
    }
}
```

