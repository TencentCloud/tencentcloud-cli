**Example 1: 批量上链接口**



Input: 

```
tccli trp CreateChainBatch --cli-unfold-argument  \
    --CorpId 1 \
    --ChainList.0.Code abc \
    --ChainList.0.Data.0.Label abc \
    --ChainList.0.Data.0.Type abc \
    --ChainList.0.Data.0.Value abc
```

Output: 
```
{
    "Response": {
        "RequestId": "abc"
    }
}
```

