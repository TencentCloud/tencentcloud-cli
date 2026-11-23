**Example 1: 创建 MCP Token**

用于获取 MCP Token

Input: 

```
tccli car CreateMCPToken --cli-unfold-argument  \
    --ExpireSeconds 50000 \
    --TokenName token*****id01 \
    --UserId v**to***_token_userid01
```

Output: 
```
{
    "Response": {
        "Token": "mcptok_1e993fa723ed62f56************************a435a95e361f11fdf49ce3c",
        "TokenId": "tok_59f*******76ee22",
        "RequestId": "4f151245-7a15-4ccf-9139-191add823c61"
    }
}
```

