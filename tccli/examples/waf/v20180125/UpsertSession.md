**Example 1: Waf  会话定义 Upsert接口**



Input: 

```
tccli waf UpsertSession --cli-unfold-argument  \
    --Domain test.com \
    --Category match \
    --KeyOrStartMat hashId \
    --EndMat end \
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
        "Data": "success",
        "RequestId": "5029e2b0-493c-4dcc-9e4e-d53ab98ede99"
    }
}
```

