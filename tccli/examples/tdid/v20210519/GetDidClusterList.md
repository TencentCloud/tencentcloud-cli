**Example 1: ClusterName**

网络基本信息

Input: 

```
tccli tdid GetDidClusterList --cli-unfold-argument ```

Output: 
```
{
    "Response": {
        "DidClusterList": [
            {
                "ChainId": 590,
                "ChainName": "DCDC",
                "AgencyCount": 2,
                "ConsortiumId": 661,
                "CreateTime": "2021-08-06 20:43:05",
                "ExpireTime": "2021-09-06 20:57:20",
                "ChainStatus": 1,
                "ResourceId": "tbaas-ijfnnzqhg6",
                "ClusterId": "bcos-8o0v0fpj12",
                "ConsortiumName": "",
                "AgencyId": 301,
                "AutoRenewFlag": 1,
                "TotalNetworkNode": 5,
                "TotalCreateNode": 4,
                "TotalGroups": 1,
                "DidCount": 5
            }
        ],
        "RequestId": "41a9acae-cef4-4949-b144-48c65ad5e425"
    }
}
```

