**Example 1: 查询主机资产**

未传 AssetType 时默认查询 host；传入 InstanceId 可定位单个实例。

Input: 

```
tccli cfw DescribeCfwAssets --cli-unfold-argument  \
    --Limit 100
```

Output: 
```
{
    "Response": {
        "Data": "{\"asset_type\":\"host\",\"assets\":[{\"instance_id\":\"ins-1\"}]}",
        "RequestId": "4266525E-10C4-41E1-8A28-5CCE1FBF6A58"
    }
}
```

