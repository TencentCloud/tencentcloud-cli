**Example 1: ModifySoftCategory**



Input: 

```
tccli ioa ModifySoftCategory --cli-unfold-argument  \
    --OsType 0 \
    --NewCategoryIdPath 7 \
    --SoftUpdateCategories.0.SoftWareId 0 \
    --SoftUpdateCategories.0.CategoryIdPath 1.6
```

Output: 
```
{
    "Response": {
        "RequestId": "dcaeacb7-4c66-4136-a9bb-c6a845c4e4d2"
    }
}
```

