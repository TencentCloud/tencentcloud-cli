**Example 1: 续费集群**



Input: 

```
tccli cynosdb RenewClusters --cli-unfold-argument  \
    --TimeUnit xx \
    --DealMode 0 \
    --ClusterId xx \
    --TimeSpan 0.0
```

Output: 
```
{
    "Response": {
        "TranId": "",
        "BigDealIds": null,
        "ResourceIds": [],
        "RequestId": "11b4ce54-xxxx",
        "ClusterIds": [],
        "DealNames": [
            "xxx",
            "xxx",
            "xxx"
        ]
    }
}
```

