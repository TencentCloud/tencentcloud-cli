**Example 1: 修改应用关联模型服务**



Input: 

```
tccli apis ModifyAgentAppModelServices --cli-unfold-argument  \
    --InstanceID ins-a7af1980 \
    --ID aga-41d42939 \
    --ModelServices.0.ID mds-ea8d96c6
```

Output: 
```
{
    "Response": {
        "Data": {
            "ID": "aga-41d42939"
        },
        "RequestId": "075b6412-222d-4994-9d93-c04d922c6b6d"
    }
}
```

