**Example 1: 应用服务解绑**



Input: 

```
tccli apis DeleteAgentAppServices --cli-unfold-argument  \
    --InstanceID ins-222fd0da \
    --ID aga-a502f357 \
    --ServiceIDs svr-17244a65
```

Output: 
```
{
    "Response": {
        "Data": {
            "ID": "aga-a502f357"
        },
        "RequestId": "e109a9fb-00c2-487c-8178-98d9c58b7628"
    }
}
```

