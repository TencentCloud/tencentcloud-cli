**Example 1: 续费集群**

续费集群

Input: 

```
tccli cynosdb RenewClusters --cli-unfold-argument  \
    --TimeUnit m \
    --DealMode 0 \
    --ClusterId cynosdbmysql-grhvkwd \
    --TimeSpan 1
```

Output: 
```
{
    "Response": {
        "BigDealIds": [
            "20241223054076837313781",
            "20241223054076837313781"
        ],
        "ClusterIds": [
            "cynosdbmysql-b6sy2i0oi"
        ],
        "DealNames": [
            "20241223054076837520111",
            "20241223054076837520121"
        ],
        "RequestId": "623f7cc5-ce5f-4f11-ad96-97bd07dad332",
        "ResourceIds": [
            "cynosdbmysql-ins-bx72i9ws",
            "cynosdbmysql-ins-i8g3n8xq"
        ],
        "TranId": ""
    }
}
```

