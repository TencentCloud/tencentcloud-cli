**Example 1: 更新集群发布序列标签**



Input: 

```
tccli tke ModifyClusterRollOutSequenceTags --cli-unfold-argument  \
    --ClusterID cls-3n90hta2 \
    --Tags.0.Key Env \
    --Tags.0.Value Test
```

Output: 
```
{
    "Response": {
        "RequestId": "f1048559-c7e4-4a7b-9d12-bc0256be3e26"
    }
}
```

