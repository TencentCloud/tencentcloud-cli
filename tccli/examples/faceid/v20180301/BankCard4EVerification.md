**Example 1: 认证通过示例**



Input: 

```
tccli faceid BankCard4EVerification --cli-unfold-argument  \
    --Name 张三 \
    --BankCard 6222222222222222222 \
    --Phone 6222222222222222222 \
    --IdCard 6222222222222222222
```

Output: 
```
{
    "Response": {
        "Result": "0",
        "Description": "认证通过",
        "RequestId": "74e742e8-f91d-49c3-9744-c20f3baca117"
    }
}
```

**Example 2: 认证不通过示例**



Input: 

```
tccli faceid BankCard4EVerification --cli-unfold-argument  \
    --Name 张三 \
    --BankCard 6222222222222222222 \
    --Phone 6222222222222222222 \
    --IdCard 6222222222222222222
```

Output: 
```
{
    "Response": {
        "Result": "-6",
        "Description": "持卡人信息有误",
        "RequestId": "24fe7851-49e9-4a4a-ac1e-3bd5c09323fd"
    }
}
```

