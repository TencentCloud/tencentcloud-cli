**Example 1: 启用集群删除保护**

集群删除保护一定程度上可以避免您误删集群，启用集群删除保护后，您将无法直接通过控制台和API来删除集群，如需删除集群，需要先关闭集群删除保护。

Input: 

```
tccli tke EnableClusterDeletionProtection --cli-unfold-argument  \
    --ClusterId cls-xxxxxxxx
```

Output: 
```
{
    "Response": {
        "RequestId": "eac6b301-a322-493a-8e36-83b295459397"
    }
}
```

