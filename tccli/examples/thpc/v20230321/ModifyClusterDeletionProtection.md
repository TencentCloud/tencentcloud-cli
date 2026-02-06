**Example 1: 关闭集群删除保护状态**



Input: 

```
tccli thpc ModifyClusterDeletionProtection --cli-unfold-argument  \
    --ClusterId hpc-cjaqo2i7 \
    --DeletionProtection OFF
```

Output: 
```
{
    "Response": {
        "RequestId": "efbbe00e-0175-4ee7-92c5-debc5763142d"
    }
}
```

