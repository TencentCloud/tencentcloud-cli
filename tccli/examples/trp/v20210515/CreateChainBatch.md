**Example 1: 批量上链接口**



Input: 

```
tccli trp CreateChainBatch --cli-unfold-argument  \
    --CorpId 10000 \
    --ChainList.0.Code https://anxin.qq.com/q99j9ovp5c6sok7l5g \
    --ChainList.0.Data.0.Label 商品名称 \
    --ChainList.0.Data.0.Type text \
    --ChainList.0.Data.0.Value 安全中心
```

Output: 
```
{
    "Response": {
        "RequestId": "eaa3ccac-d2f5-4df0-a8b3-7b51324e9283"
    }
}
```

