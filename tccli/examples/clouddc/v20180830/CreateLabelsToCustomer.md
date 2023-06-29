**Example 1: 示例**



Input: 

```
tccli clouddc CreateLabelsToCustomer --cli-unfold-argument  \
    --Industry 1 \
    --SubIndustry 2 \
    --LabelKey GUOQI \
    --Cids ab081cb3b68e28f1e184e9f8dc3ab448 d1d7383e67b82aa9116d229bde649862 \
    --RequestFrom 1
```

Output: 
```
{
    "Response": {
        "JsonString": "[{\"code\":200047,\"msg\":\"\\u5ba2\\u6237\\u6807\\u7b7e\\uff1a\\u6218\\u7565\\u5730\\u56fe\\u5ba2\\u6237\\u5df2\\u6253\\u6807\\u5728\\u6d4b\\u8bd5\\u5ba2\\u6237\\u540d\\u79f01\\u5ba2\\u6237\\u4e0a\",\"cid\":\"ab081cb3b68e28f1e184e9f8dc3ab448\"},{\"cid\":\"d1d7383e67b82aa9116d229bde649862\",\"code\":0,\"msg\":\"ok\"}]",
        "RequestId": "533f4300-d580-40f5-b4b5-021231bc23fb"
    }
}
```

