**Example 1: GetDataPanel**

概览

Input: 

```
tccli tdid GetDataPanel --cli-unfold-argument  \
    --ClusterId 1
```

Output: 
```
{
    "Response": {
        "BlockNetworkCount": 1,
        "BlockNetworkName": "name",
        "BlockHeight": 1,
        "BlockNetworkType": 1,
        "DidCount": 15,
        "CptCount": 10,
        "CertificatedAuthCount": 1,
        "IssueCptCount": 1,
        "NewDidCount": 15,
        "BcosCount": 10,
        "FabricCount": 1,
        "ChainMakerCount": 1,
        "RequestId": "eac6b301-a322-493a-8e36-83b295459397"
    }
}
```

