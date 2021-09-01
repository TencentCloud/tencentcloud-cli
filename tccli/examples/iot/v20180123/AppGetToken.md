**Example 1: 获取用户token**

获取用户token

Input: 

```
tccli iot AppGetToken --cli-unfold-argument  \
    --UserName iotappuser \
    --Password iotappuser666! \
    --Expire 86400
```

Output: 
```
{
    "Response": {
        "RequestId": "96d63e89-5702-4047-8607-35caca174119",
        "AccessToken": "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJpZCI6ImFwcC1od2dhYjQxeVwvdXNlcm5hbWUiLCJ2ZXIiOiJjODhlZTM4NjQwMmMiLCJleHBfYXQiOjE1MjUyNjU3NTd9.rRTE6BpxYvK3X1IfjAf6jTvh97ZqKd4CUQlXq8vmWSg"
    }
}
```

