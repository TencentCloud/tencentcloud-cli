**Example 1: 请求删除Index为1的推流配置**



Input: 

```
tccli live DeleteCasterOutputInfo --cli-unfold-argument  \
    --OutputIndex 1 \
    --CasterId 1234
```

Output: 
```
{
    "Response": {
        "RequestId": "3c140219-cfe9-470e-b241-907877d6fb03"
    }
}
```

