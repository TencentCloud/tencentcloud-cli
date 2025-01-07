**Example 1: 获取用户信息**



Input: 

```
tccli lcic DescribeUser --cli-unfold-argument  \
    --UserId 2kJJBH6G1dfBFUJqXLh0Mg3ELLk
```

Output: 
```
{
    "Response": {
        "SdkAppId": 1,
        "UserId": "2kJJBH6G1dfBFUJqXLh0Mg3ELLk",
        "Name": "zhagnsan",
        "Avatar": "https://xxx.com/cat.jpg",
        "OriginId": "hello-moto",
        "RequestId": "2a117d109a0c533e5ecd37fc221ba7f7"
    }
}
```

