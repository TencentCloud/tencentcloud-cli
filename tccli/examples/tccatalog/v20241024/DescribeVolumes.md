**Example 1: 获取volume**



Input: 

```
tccli tccatalog DescribeVolumes --cli-unfold-argument  \
    --CatalogName c1 \
    --SchemaName s1 \
    --VolumeNames v1
```

Output: 
```
{
    "Response": {
        "Volumes": null,
        "RequestId": "b029fc77-140b-44ae-80bf-b01b40d5ddcc"
    }
}
```

