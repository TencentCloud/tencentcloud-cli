**Example 1: 申请CSR**

申请CSR

Input: 

```
tccli ssl CreateCSR --cli-unfold-argument  \
    --Domain www.***.com \
    --Organization Tencent \
    --Department It \
    --Email abc@qq.com \
    --Province Hunan \
    --City Changsha \
    --Country China \
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

