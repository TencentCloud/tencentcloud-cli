**Example 1: 查看集群镜像是否能够升级**



Input: 

```
tccli dlc CheckDataEngineImageCanBeUpgrade --cli-unfold-argument  \
    --DataEngineId DataEngine-1
```

Output: 
```
{
    "Response": {
        "ChildImageVersionId": "d3ftghd4-9a7e-4f64-a3f4-f38507c69742",
        "IsUpgrade": true,
        "RequestId": "b8sd7dd7-ekd4-4e5e-993e-e5db64fa21c1"
    }
}
```

