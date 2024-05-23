**Example 1: 实例一**



Input: 

```
tccli dlc AddOptimizerEngines --cli-unfold-argument  \
    --Catalog DataLakeCatalog \
    --Engines.0.HouseName abc \
    --Engines.0.HouseId abc \
    --Engines.0.HouseSize 0 \
    --Database mydb \
    --Table mytb
```

Output: 
```
{
    "Response": {
        "RequestId": "1304581893_25027_1709796072623_223"
    }
}
```

