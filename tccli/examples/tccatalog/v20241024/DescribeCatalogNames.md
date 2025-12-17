**Example 1: 列出所有数据目录名称**



Input: 

```
tccli tccatalog DescribeCatalogNames --cli-unfold-argument  \
    --CatalogNamePattern LaYyu_c%
```

Output: 
```
{
    "Response": {
        "CatalogNames": [
            {
                "Name": "layyu_c1",
                "Namespace": []
            }
        ],
        "RequestId": "6708d9a9-92ae-4a6a-90d4-7488acd53245"
    }
}
```

