**Example 1: ModifySubscriber示例**



Input: 

```
tccli tccatalog ModifySubscriber --cli-unfold-argument  \
    --SubscriberId d47622ad-b8dc-4385-862e-bcdb6f7a275e \
    --Filters.0.Name Operation \
    --Filters.0.Values ALTER_METALAKE CREATE_TABLE DROP_TABLE \
    --Filters.1.Name Identifier \
    --Filters.1.Values catalog_006 catalog_006.db001 catalog_006.default.jinyu *.*.* *.* *
```

Output: 
```
{
    "Response": {
        "RequestId": "helllllllo"
    }
}
```

