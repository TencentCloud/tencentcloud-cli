**Example 1: 获取临时实例访问凭证**

获取实例的临时访问凭证，有效期仅 1 小时，可用于临时登录。

Input: 

```
tccli tcr CreateInstanceToken --cli-unfold-argument  \
    --RegistryId tcr-dg284imq \
    --TokenType temp \
    --Desc desc
```

Output: 
```
{
    "Response": {
        "ExpTime": 1735880997750,
        "RequestId": "bfa74e4d-3cc2-45a0-980c-08f7ec527737",
        "Token": "eyJhbGciOiJSUzI1NiIsImtpZCI6IlhETVk6VFVWTDo2SlRVOkxPSEE6M1VGVTozWFhJOlM3RkI6TlA3MjozTVYyOlRBQlQ6REdCQzpEQzNIIn0.eyJvd25lclVpbiI6IjMzMjEzMzc5OTQiLCJvcGVyYXRvclVpbiI6IjEwMDAzNjk1MDIzNCIsImV4cCI6MTczNTg4MDk5NywibmJmIjoxNzM1ODc3Mzk3LCJpYXQiOjE3MzU4NzczOTd9.vfgpeIog2z_cSTQnfWEh3jykmKNJ57b2hU-MciSuS3c9tiuju4Q-i_yPBjpDzHr-zymPsxmvFmyPV5Bxtv2UIvAfrk27ZnWUWf8xxF70D7BnY2PO6lSgUqGK0H2lw8HvYMq7JZjGk_q_eHcGQTLiY_-15HLNWjjL2Kvn5sybzaPx7-ZB4efa1WLOdB9rHQRwqmGuBaJaFTkpVZpJ0gRBF6hj7xq-ozjJVurXO1FFjC8DINJt0FvKt3U7VdhVAR2xTUHp54Dz4Q0Nynl5OoaBzYbVuobN5e_VerrYL-UAIu3PU3z7oZFNCCn3JeySbNThofubRW5M1DObxiPsjVSLdA",
        "TokenId": "",
        "Username": "100036950234"
    }
}
```

**Example 2: 获取长期实例访问凭证**

获取实例的长期有效的访问凭证，可用于第三方应用授权。

Input: 

```
tccli tcr CreateInstanceToken --cli-unfold-argument  \
    --RegistryId tcr-dg284imq \
    --TokenType longterm \
    --Desc desc
```

Output: 
```
{
    "Response": {
        "ExpTime": 2051237057817,
        "RequestId": "116b7c24-58af-452a-9d91-bdfc988a56ec",
        "Token": "eyJhbGciOiJSUzI1NiIsImtpZCI6IlhETVk6VFVWTDo2SlRVOkxPSEE6M1VGVTozWFhJOlM3RkI6TlA3MjozTVYyOlRBQlQ6REdCQzpEQzNIIn0.eyJvd25lclVpbiI6IjMzMjEzMzc5OTQiLCJvcGVyYXRvclVpbiI6IjEwMDAzNjk1MDIzNCIsInRva2VuSWQiOiJjdHJtM2c4Nmg3Y3Axa2I3ZWwyZyIsImV4cCI6MjA1MTIzNzA1NywibmJmIjoxNzM1ODc3MDU3LCJpYXQiOjE3MzU4NzcwNTd9.PSZiX0ZAEvAo6lbhrUypAyII12hey2SE08pL4J5_7kBNJQdpSK-Ersw5YWuO1j90xXb6rWBuLPmCqUEA-Gg4Xla2yCWlT4eF2ls2HFKUlA8gxVoGmaFN3ww6yyImC4i1o9guPSUl2ggI3k_ohSkpaooDnKPpUzBDfqptgd-ZHrNAsqlNloQISggFzIhfZiR9c4rrnxp-a7_Q0phR24uY5X0C3lYQYYFDph-SlQ9BgFRGLBUw1IUcTVZ57uXLcFis9XsazFVyFvXtOUwGfHQ5DIb5B8mReJg7XKMgG1RfpsngSF-y0QR12OKIyNvHl8Ty-HXU-J0hDm1HWKDhM-mXcQ",
        "TokenId": "ctrm3g86h7cp1kb7el2g",
        "Username": "100036950234"
    }
}
```

