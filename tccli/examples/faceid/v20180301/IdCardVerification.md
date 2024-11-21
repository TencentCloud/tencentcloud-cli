**Example 1: 身份信息认证一致示例**



Input: 

```
tccli faceid IdCardVerification --cli-unfold-argument  \
    --IdCard 11204416541220243X \
    --Name 韦小宝
```

Output: 
```
{
    "Response": {
        "Result": "0",
        "Description": "姓名和身份证号一致",
        "RequestId": "94b54cdf-d975-4718-b091-32f8d79d6397"
    }
}
```

**Example 2: 身份信息认证不一致示例**



Input: 

```
tccli faceid IdCardVerification --cli-unfold-argument  \
    --IdCard 440305199505132561 \
    --Name 刘洋
```

Output: 
```
{
    "Response": {
        "Result": "-1",
        "Description": "姓名和身份证号不一致",
        "RequestId": "80c7abb8-4563-4636-98c3-0499f1611a33"
    }
}
```

