**Example 1: 预付费集群转后付费集群**

预付费集群转后付费集群

Input: 

```
tccli cynosdb TransferClusterPrepayToPostpay --cli-unfold-argument  \
    --ClusterId cynosdbmysql-3xazs3u5
```

Output: 
```
{
    "Response": {
        "BigDealIds": [
            "20260716054021858214051"
        ],
        "TranId": "20260716054021858214051",
        "DealNames": [
            "20260716054021858214051"
        ],
        "ResourceIds": [
            "cynosdbmysql-3xazs3u5"
        ],
        "ClusterIds": [
            "cynosdbmysql-3xazs3u5"
        ],
        "RequestId": "sjhkuyfa348969-fsfsdf"
    }
}
```

