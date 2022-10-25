**Example 1: 聚鑫-创建子商户**



Input: 

```
tccli cpdp CreateCloudSubMerchant --cli-unfold-argument  \
    --MidasEnvironment sandbox \
    --MidasAppId demo001 \
    --SubMchDescription xxx \
    --SubMchName demos001 \
    --SubMchShortName ds001 \
    --OutSubMerchantId osm001 \
    --ParentAppId demo001
```

Output: 
```
{
    "Response": {
        "ChannelAppId": "xx",
        "Level": 1,
        "RequestId": "dd242838-4241-459b-b138-8f29e4fabbaa",
        "SubAppId": "sub-11297",
        "ChannelSubMerchantId": "abc001220413"
    }
}
```

