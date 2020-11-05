**Example 1: Querying purchasable subscription region**



Input: 

```
tccli dts DescribeRegionConf --cli-unfold-argument ```

Output: 
```
{
    "Response": {
        "TotalCount": 1,
        "Items": [
            {
                "RegionName": "Guangzhou",
                "Region": "ap-guangzhou",
                "Area": "South China",
                "IsDefaultRegion": 1,
                "Status": 1
            }
        ]
    }
}
```

