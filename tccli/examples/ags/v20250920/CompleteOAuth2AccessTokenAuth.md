**Example 1: 确认OAuth2 session完成授权**



Input: 

```
tccli ags CompleteOAuth2AccessTokenAuth --cli-unfold-argument  \
    --SessionUri urn:ietf:params:oauth:request_uri:d********************7a042c70a0c******************106b6f0ca2969e \
    --UserId ********
```

Output: 
```
{
    "Response": {
        "RequestId": "250a63d7-e15c-45c2-a83b-1f80b55d93ce"
    }
}
```

