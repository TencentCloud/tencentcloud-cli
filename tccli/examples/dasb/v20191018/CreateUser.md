**Example 1: 新建用户**

新建用户

Input: 

```
tccli dasb CreateUser --cli-unfold-argument  \
    --UserName zhangsan \
    --ValidateTo 2020-09-22T00:00:00+00:00 \
    --RealName zhangsan \
    --GroupIdSet 1 1 1 \
    --Phone 138*** \
    --ValidateFrom 2020-09-22T00:00:00+00:00 \
    --Email 168***@qq.com \
    --AuthType 1
```

Output: 
```
{
    "Response": {
        "Id": 1,
        "RequestId": "dfac9070-8b23-499e-83b2-a50e3ca059af"
    }
}
```

