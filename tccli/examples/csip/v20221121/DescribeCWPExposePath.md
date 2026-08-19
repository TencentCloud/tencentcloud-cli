**Example 1: 主机资产暴露路径**



Input: 

```
tccli csip DescribeCWPExposePath --cli-unfold-argument  \
    --AssetID ins-m5ys3f8k \
    --AssetAppID 1300448058 \
    --Ip 1.1.1.1 \
    --Domain t.com \
    --Port 80 \
    --MemberId mem-*en*ent-6*5795*52f*6e4*9
```

Output: 
```
{
    "Response": {
        "Content": "",
        "RequestId": "a27477c4-b02d-4159-8af3-6f72fa874cd8"
    }
}
```

