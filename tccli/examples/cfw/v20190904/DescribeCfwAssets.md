**Example 1: 使用 NextToken 续查资产或指纹**

资产或指纹续查都只传 NextToken，不要解析或构造 token；HasMore=false 时结束。

Input: 

```
tccli cfw DescribeCfwAssets --cli-unfold-argument  \
    --NextToken opaque-token
```

Output: 
```
{
    "Response": {
        "Data": "{\"asset_type\":\"host\",\"assets\":[{\"instance_id\":\"ins-xxxxxxxx\",\"fingerprints\":[{\"port\":80}]}],\"HasMore\":false}",
        "RequestId": "4266525E-10C4-41E1-8A28-5CCE1FBF6A58"
    }
}
```

**Example 2: 精确查询实例及指纹**

exact InstanceId 每页重复基础资产，fingerprints 仅为当前页；HasMore=true 时使用 NextToken 续查剩余指纹。

Input: 

```
tccli cfw DescribeCfwAssets --cli-unfold-argument  \
    --AssetType host \
    --InstanceId ins-xxxxxxxx
```

Output: 
```
{
    "Response": {
        "Data": "{\"asset_type\":\"host\",\"assets\":[{\"instance_id\":\"ins-xxxxxxxx\",\"fingerprints\":[{\"port\":443}]}],\"HasMore\":true,\"NextToken\":\"opaque-token\"}",
        "RequestId": "4266525E-10C4-41E1-8A28-5CCE1FBF6A58"
    }
}
```

**Example 3: 首次查询主机资产**

broad host 列表返回基础资产；如果 Data.HasMore 为 true，保存 Data.NextToken。

Input: 

```
tccli cfw DescribeCfwAssets --cli-unfold-argument  \
    --AssetType host \
    --Limit 20
```

Output: 
```
{
    "Response": {
        "Data": "{\"asset_type\":\"host\",\"assets\":[{\"instance_id\":\"ins-1\"}],\"HasMore\":true,\"NextToken\":\"opaque-token\"}",
        "RequestId": "4266525E-10C4-41E1-8A28-5CCE1FBF6A58"
    }
}
```

