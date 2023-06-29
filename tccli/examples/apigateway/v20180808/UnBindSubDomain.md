**Example 1: 解绑自定义域名**

服务解绑自定义域名

Input: 

```
tccli apigateway UnBindSubDomain --cli-unfold-argument  \
    --ServiceId service-19c5fnhy \
    --SubDomain app01.sevenlayer23.com
```

Output: 
```
{
    "Response": {
        "Result": true,
        "RequestId": "b3197c48-53fb-46df-b721-df4424cf8be9"
    }
}
```

