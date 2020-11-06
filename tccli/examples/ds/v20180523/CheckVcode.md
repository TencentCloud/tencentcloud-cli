**Example 1: 检测验证码**

检测验证码

Input: 

```
tccli ds CheckVcode --cli-unfold-argument  \
    --Module VerifyCode \
    --Operation CheckVcode \
    --AccountResId dcu-c33uil4ap6 \
    --ContractResId dcc-79dlei3yb6 \
    --VerifyCode 243545
```

Output: 
```
{
    "Response": {
        "RequestId": "92f683e1-45e4-47f0-bfa3-d1831b1c1342"
    }
}
```

