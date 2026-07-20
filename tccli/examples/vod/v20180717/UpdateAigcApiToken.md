**Example 1: 更新ip限制**



Input: 

```
tccli vod UpdateAigcApiToken --cli-unfold-argument  \
    --SubAppId 251441341 \
    --ApiToken D2JJ0DHJ********************rXFX \
    --ActionType Merge \
    --ExtInfo {"ip":{"9.134.4.21":true}}
```

Output: 
```
{
    "Response": {
        "RequestId": "96a1da82-7443-4765-82e4-c1065959f908"
    }
}
```

