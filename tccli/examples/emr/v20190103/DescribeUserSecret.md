**Example 1: 获取用户密码**



Input: 

```
tccli emr DescribeUserSecret --cli-unfold-argument  \
    --User test \
    --SecretType pwd
```

Output: 
```
{
    "Response": {
        "RequestId": "abc"
    }
}
```

