**Example 1: 修改CSR**

修改CSR

Input: 

```
tccli ssl ModifyCSR --cli-unfold-argument  \
    --CSRId 662 \
    --Generate False \
    --Domain hywh**.com \
    --Organization tencent \
    --Department it \
    --Email heysh**hhe@qq.com \
    --Province hunan \
    --City changsha \
    --Country china \
    --EncryptAlgo RSA \
    --KeyParameter 2048
```

Output: 
```
{
    "Response": {
        "Id": 662,
        "RequestId": "f00f136b-c0c8-476a-8097-b1bdfc9d330f"
    }
}
```

