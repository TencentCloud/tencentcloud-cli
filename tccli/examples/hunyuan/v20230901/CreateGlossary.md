**Example 1: 创建术语库**



Input: 

```
tccli hunyuan CreateGlossary --cli-unfold-argument  \
    --Name 我的术语库 \
    --Source en \
    --Target zh
```

Output: 
```
{
    "Response": {
        "GlossaryId": "6df696144203027ba838dbfb5b8c2fba",
        "Name": "我的术语库",
        "RequestId": "e53930ed-b529-42f8-a933-b4a773587c4c"
    }
}
```

