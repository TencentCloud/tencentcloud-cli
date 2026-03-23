**Example 1: 创建应用关联模型服务**



Input: 

```
tccli apis CreateAgentAppModelServices --cli-unfold-argument  \
    --InstanceID ins-a7af1980 \
    --ID aga-41d42939 \
    --ModelServices.0.ID mds-ea8d96c6 \
    --ModelServices.0.InvokeLimitConfigStatus False
```

Output: 
```
{
    "Response": {
        "Data": {
            "ID": "aga-41d42939"
        },
        "RequestId": "6a58841b-8aca-43bb-8894-8b9e65619267"
    }
}
```

