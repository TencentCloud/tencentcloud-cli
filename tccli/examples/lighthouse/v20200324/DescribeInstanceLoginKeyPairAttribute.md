**Example 1: 查询实例默认登录密钥属性**



Input: 

```
tccli lighthouse DescribeInstanceLoginKeyPairAttribute --cli-unfold-argument  \
    --InstanceId lhins-j4liwha8
```

Output: 
```
{
    "Response": {
        "PermitLogin": "NO",
        "RequestId": "17a8c37b-0901-402a-b7b2-357998b2bcd8"
    }
}
```

