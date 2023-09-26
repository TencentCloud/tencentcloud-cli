**Example 1: Waf  会话定义 Upsert接口**



Input: 

```
tccli waf UpsertSession --cli-unfold-argument  \
    --Domain test.com \
    --Category match \
    --KeyOrStartMat hashId \
    --EndMat 12 \
    --Source get \
    --StartOffset -1 \
    --EndOffset -1 \
    --Edition clb-waf \
    --SessionName 测试SESSION
```

Output: 
```
{
    "Response": {
        "Data": "",
        "RequestId": "abc"
    }
}
```

