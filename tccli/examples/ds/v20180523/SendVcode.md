**Example 1: 发送验证码**

发送验证码

Input: 

```
tccli ds SendVcode --cli-unfold-argument  \
    --Module VerifyCode \
    --Operation SendVcode \
    --ContractResId dcc-79dlei3yb6 \
    --AccountResId dcu-c33uil4ap6
```

Output: 
```
{
    "Response": {
        "RequestId": "7fb52b2f-edfc-432b-a51f-690a2bdfc4d4"
    }
}
```

