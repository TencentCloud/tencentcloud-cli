**Example 1: 修改用户信息**

修改用户信息

Input: 

```
tccli dasb ModifyUser --cli-unfold-argument  \
    --Id 1 \
    --ValidateTo 2020-09-22T00:00:00+00:00 \
    --RealName zhangsan \
    --GroupIdSet 1 2 3 \
    --Phone 183***98 \
    --ValidateFrom 2020-09-22T00:00:00+00:00 \
    --Email test@qq.com
```

Output: 
```
{
    "Response": {
        "RequestId": "dfac9070-8b23-499e-83b2-a50e3ca059af"
    }
}
```

