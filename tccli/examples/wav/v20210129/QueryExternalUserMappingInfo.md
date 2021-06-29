**Example 1: 外部联系人转换接口**



Input: 

```
tccli wav QueryExternalUserMappingInfo --cli-unfold-argument  \
    --CorpExternalUserIdList wmQIM2CwAAywHqH07voRw9aacKXf09eQ wmAA2CCwAAywHqH07voRw9aacAFEewf
```

Output: 
```
{
    "Response": {
        "ExternalUserIdMapping": [
            {
                "CorpExternalUserId": "wmabc2CAAATGwpQTxuU1IaaaiOFH2cXA",
                "ExternalUserId": "wmpqy2CAAATGwpQTxuU1IUfoiOFH2cXA"
            }
        ],
        "RequestId": "b1a024bf-4d74-4b5d-a5bd-bbec330520e8"
    }
}
```

