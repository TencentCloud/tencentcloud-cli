**Example 1: CreateMpCrowdPack**



Input: 

```
tccli zj CreateMpCrowdPack --cli-unfold-argument  \
    --License KA3431QZPU \
    --Name 测试人群包 \
    --FileName test.txt \
    --Desc demo \
    --CosUrl /account/111/file \
    --MpId 999 \
    --AppName 腾讯珠玑
```

Output: 
```
{
    "Response": {
        "Data": {
            "ID": 100
        },
        "RequestId": "111111"
    }
}
```

