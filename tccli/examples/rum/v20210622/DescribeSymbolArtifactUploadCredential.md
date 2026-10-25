**Example 1: 获取上传凭证**



Input: 

```
tccli rum DescribeSymbolArtifactUploadCredential --cli-unfold-argument  \
    --Kind js_sourcemap \
    --FileName demo.min.js \
    --AppId ****** \
    --Release npm-demo-1.0.6-ip202 \
    --MinifiedUrl http://127.0.0.1:4173/demo.min.js \
    --FileType minified \
    --ContentType application/json \
    --ProjectId ******
```

Output: 
```
{
    "Response": {
        "Result": "{\"bucket\":\"***************\",\"cos_key\":\"sourcemaps/146683/npm************ip202/_/dbff70a41************41998988***************\",\"cos_url\":\"https://*********************************************/sourcemaps/**************************************************************************\",\"expiration\":\"2026-07-09T07:27:12Z\",\"expired_time\":1783582032,\"region\":\"ap-guangzhou\",\"session_token\":\"Ei1QfCjWZztAZjAQ5rCjGh3UhKCuOXEac820d4ce2306e4254c91e150f5f4d86agyNg2CfPAt14Y8ptEsPGv5IlhYPGDMDhR3k6x42eaCbnTWE7NH2ywBHGj8tAwbEDl4i4xP26mo_yA3PlHOldoG6mI-RsqaKl70lYMDk3f2bjFbiYuXs3e-mEo4VA-28u97axxVo_kdBjTSzTzV1EJgfmXlf1wsOHel2889OoFoNX4J9phsQXR0K2HCdkRshVKtiod6isuqYKQ0UEhPasRzK38bykpgRt_CS3LgWwlIwSEdyOtlnW8L5nVBgpcYfLVqwF2YflB_unCTjSIrgvAUSQxSzOH08VaLcUhUlns1LeAO3OO4DOMnxovOlGcKUXBbXsC0IYTwWgvZjSGa6QpOwNewq_14mygI7oKHXkxOjIT7PahynTGnxFjBXxomz9gyPPpD0ebmvt5mjOofL_8RyJFWm89eVzzBkU2nHiRxxFnQbx8m8p9L2aOaMOvN_GWhHVZySnkyn8PfE5mLz3FSsVERgULcK4iVYgW5Lfd8qrx9u3Nc1IroWHaemYXNGUBQGseutONRoNUyvGdivNpHCKXxhH_rQ7n6wZn5_WsimzYlJyNdXtjxt_H4_XIXonDEzTqK5sXXkgfDNq8IThGkOp9gH_BwwjGxzktRgOzMeGt8FAj_7QEDW1SFRPlvyr2F9_WeMDQZEKByDKIqA2vF8v5xWrOQc_OAISp1LQ5Wbsb21GC-zyOVGi6BEKLL1RktxwAE1RDtk0ZZVWA8hOSg\",\"start_time\":1783581132,\"sts_request_id\":\"d8d12df1-40c4-4ad8-9187-041cfae1b8f7\",\"tmp_secret_id\":\"********************************************************************\",\"tmp_secret_key\":\"********************************************\"}",
        "RequestId": "7101c383-3be4-4cd1-85d3-5d8f94e59882"
    }
}
```

