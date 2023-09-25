**Example 1: 无效id**



Input: 

```
tccli bi DeleteDatasource --cli-unfold-argument  \
    --ProjectId 1 \
    --Id 1
```

Output: 
```
{
    "Response": {
        "RequestId": "9b37bc0d-2a4d-40f0-a620-3a962872aecf",
        "Extra": "",
        "Data": "",
        "Msg": "非法的数据源ID"
    }
}
```

**Example 2: success**



Input: 

```
tccli bi DeleteDatasource --cli-unfold-argument  \
    --ProjectId 1 \
    --Id 56
```

Output: 
```
{
    "Response": {
        "RequestId": "9c22f4d3-e28c-450d-8c9f-2e72c40b7001",
        "Extra": "",
        "Data": null,
        "Msg": "success"
    }
}
```

