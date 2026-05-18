**Example 1: 获取地域配置**

获取地域配置

Input: 

```
tccli cdb DescribeRegion --cli-unfold-argument  \
    --MasterRegion ap-guangzhou \
    --IsDr 0 \
    --IsRo 0 \
    --MasterZone ap-guangzhou-3
```

Output: 
```
{
    "Response": {
        "Regions": [],
        "Configs": [],
        "RequestId": ""
    }
}
```

