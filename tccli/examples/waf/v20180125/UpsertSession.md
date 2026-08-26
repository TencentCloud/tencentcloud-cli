**Example 1: 新增会话定义**



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
        "SessionID": 200000001,
        "RequestId": "5029e2b0-493c-4dcc-9e4e-d53ab98ede99"
    }
}
```

