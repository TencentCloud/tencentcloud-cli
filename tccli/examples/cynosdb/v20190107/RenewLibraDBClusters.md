**Example 1: 续费分析集群**



Input: 

```
tccli cynosdb RenewLibraDBClusters --cli-unfold-argument  \
    --TimeSpan 1 \
    --TimeUnit m \
    --ClusterId libradb-2yza6dpd
```

Output: 
```
{
    "Response": {
        "BigDealIds": [
            "20250624625002997262491"
        ],
        "ClusterIds": [],
        "DealNames": [
            "20250624625002997244161"
        ],
        "RequestId": "6aaf5b2f-1dc2-46fc-93c6-74921cb996bd",
        "ResourceIds": [],
        "TranId": ""
    }
}
```

