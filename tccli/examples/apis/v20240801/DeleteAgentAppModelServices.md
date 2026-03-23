**Example 1: 删除应用关联模型服务**



Input: 

```
tccli apis DeleteAgentAppModelServices --cli-unfold-argument  \
    --InstanceID ins-a7af1980 \
    --ID aga-41d42939 \
    --ModelServiceIDs mds-ea8d96c6
```

Output: 
```
{
    "Response": {
        "Data": {
            "ID": "aga-41d42939"
        },
        "RequestId": "02dd3ade-7813-4f83-9024-5948f207e02c"
    }
}
```

