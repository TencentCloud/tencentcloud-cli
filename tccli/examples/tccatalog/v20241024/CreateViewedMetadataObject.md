**Example 1: 把test.test加入最近浏览**



Input: 

```
tccli tccatalog CreateViewedMetadataObject --cli-unfold-argument  \
    --FullName test.test \
    --Type schema
```

Output: 
```
{
    "Response": {
        "RequestId": "a91c1afa-f84a-402c-ac01-d6c00eaaebd1",
        "ViewedMetadataObject": {
            "FullName": "test.test",
            "LastViewedTime": "2024-12-17 16:27:08",
            "Type": "schema"
        }
    }
}
```

