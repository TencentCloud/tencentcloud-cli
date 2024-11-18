**Example 1: 查询密码破解状态**



Input: 

```
tccli cwp DescribePasswordCrackStatus --cli-unfold-argument  \
    --Password admin
```

Output: 
```
{
    "Response": {
        "HasCracked": true,
        "RequestId": "da7cc6e2-c4b3-42b4-9183-a8d0c86f2c70"
    }
}
```

