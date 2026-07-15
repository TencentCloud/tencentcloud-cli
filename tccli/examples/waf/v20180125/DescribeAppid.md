**Example 1: 根据ip查找一条appid情况1**

存在地域为Zone的IP，也能根据IP正常找到Appid；

Input: 

```
tccli waf DescribeAppid --cli-unfold-argument  \
    --IP 139.199.91.148
```

Output: 
```
{
    "Response": {
        "Appid": 251000863,
        "RequestId": "b4f13899-561b-46a0-a045-132312123"
    }
}
```

**Example 2: 根据ip查找一条appid情况2**

不存在地域为Zone的IP，返回内部错误；

Input: 

```
tccli waf DescribeAppid --cli-unfold-argument  \
    --IP 139.199.91.148
```

Output: 
```
{
    "Response": {
        "Appid": 251000863,
        "RequestId": "b4f13899-561b-46a0-a045-132312122"
    }
}
```

**Example 3: 根据ip查找一条appid情况3**

存在地域为Zone的IP，但无法根据IP查找到对应的Appid，返回0

Input: 

```
tccli waf DescribeAppid --cli-unfold-argument  \
    --IP 139.199.91.31
```

Output: 
```
{
    "Response": {
        "Appid": 0,
        "RequestId": "a2a51726-ac95-473d-89fc-954d36428590"
    }
}
```

