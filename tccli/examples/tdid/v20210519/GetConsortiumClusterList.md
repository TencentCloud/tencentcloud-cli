**Example 1: GetConsortiumList**

获取联盟列表

Input: 

```
tccli tdid GetConsortiumClusterList --cli-unfold-argument  \
    --ConsortiumId 661
```

Output: 
```
{
    "Response": {
        "ClusterList": [
            {
                "ChainId": 591,
                "ChainName": "asdfafffffffffffffffffffffff",
                "AgencyCount": 2,
                "ConsortiumId": 661,
                "CreateTime": "2021-08-07 15:40:46",
                "ExpireTime": "2021-09-07 15:53:55",
                "ChainStatus": 1,
                "ResourceId": "tbaas-6s0ih1k0rg",
                "ClusterId": "bcos-03z30qbg1c",
                "ConsortiumName": "TDID测试",
                "AgencyId": 303,
                "AutoRenewFlag": 1,
                "TotalNetworkNode": 5,
                "TotalCreateNode": 5,
                "TotalGroups": 28
            }
        ],
        "RequestId": "41a9acae-cef4-4949-b144-48c65ad5e425"
    }
}
```

