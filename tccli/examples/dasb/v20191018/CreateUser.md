**Example 1: 新建用户**

新建用户

Input: 

```
tccli dasb CreateUser --cli-unfold-argument  \
    --UserName test \
    --ValidateTo 2020-09-22T00:00:00+00:00 \
    --RealName test \
    --GroupIdSet 1 1 1 \
    --Phone 13811111111 \
    --ValidateFrom 2020-09-22T00:00:00+00:00 \
    --Email test@qq.com \
    --AuthType 1
```

Output: 
```
{
    "Response": {
        "Id": 1,
        "RequestId": "123"
    }
}
```

