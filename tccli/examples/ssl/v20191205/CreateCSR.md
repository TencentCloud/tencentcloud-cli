**Example 1: 申请CSR**

申请CSR

Input: 

```
tccli ssl CreateCSR --cli-unfold-argument  \
    --Domain abc12 \
    --Organization abc12 \
    --Department abc12 \
    --Email abc@qq.com \
    --Province abc \
    --City abc \
    --Country abc \
    --EncryptAlgo ECC \
    --KeyParameter prime256v1 \
    --Generate False
```

Output: 
```
{
    "Response": {
        "Id": 733,
        "RequestId": "f00f136b-c0c8-476a-8097-b1bdfc9d330f"
    }
}
```

