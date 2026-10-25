**Example 1: 修改数据目录信息**

修改数据目录的注释

Input: 

```
tccli databuddy UpdateCatalog --cli-unfold-argument  \
    --CatalogName my_catalog \
    --NewComment updated catalog comment \
    --WorkspaceId 17697667906247629
```

Output: 
```
{
    "Response": {
        "Data": {
            "Result": true
        },
        "RequestId": "d10bdfbd-8f87-4ce4-9172-023775de61f9"
    }
}
```

