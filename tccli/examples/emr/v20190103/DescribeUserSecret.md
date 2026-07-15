**Example 1: 获取用户密码**



Input: 

```
tccli emr DescribeUserSecret --cli-unfold-argument  \
    --InstanceId emr-xxx \
    --User testuser \
    --SecretType pwd
```

Output: 
```
{
    "Response": {
        "Principal": "",
        "Secret": "fadadafd",
        "RequestId": "abcfafdaafasda"
    }
}
```

