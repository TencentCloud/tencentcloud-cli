**Example 1: 关闭IDC集群专线代理**

关闭IDC集群的专线/VPN代理，释放终端节点资源。

Input: 

```
tccli thpc DisableClusterDedicatedProxy --cli-unfold-argument  \
    --ClusterId hpc-12345678
```

Output: 
```
{
    "Response": {
        "RequestId": "b2ac2379-6453-4eab-8f63-7ade00cb67b0"
    }
}
```

