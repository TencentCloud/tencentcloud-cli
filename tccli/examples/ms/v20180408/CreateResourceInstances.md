**Example 1: 创建加固资源**

白名单用户通过创建加固资源自己加固。

Input: 

```
tccli ms CreateResourceInstances --cli-unfold-argument  \
    --Pid 12750 \
    --TimeUnit m \
    --TimeSpan 6 \
    --ResourceNum 10
```

Output: 
```
{
    "Response": {
        "RequestId": "2dfd3c41-5606-446f-a437-ca7bbbe07b26",
        "ResourceSet": [
            "mspro_20180913_6b2787b5_0",
            "mspro_20180913_6b2787b5_1",
            "mspro_20180913_6b2787b5_2",
            "mspro_20180913_6b2787b5_3",
            "mspro_20180913_6b2787b5_4"
        ]
    }
}
```

