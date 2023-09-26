**Example 1: CNAME 接入时，验证域名归属权**

验证域名 test.example.com 的归属权。

Input: 

```
tccli teo VerifyOwnership --cli-unfold-argument  \
    --Domain test.example.com
```

Output: 
```
{
    "Response": {
        "Status": "success",
        "Result": "",
        "RequestId": "9kl50bew-89ga-44f4-91ce-78125d53vd2a"
    }
}
```

**Example 2: CNAME 接入时，验证站点归属权**

验证站点 example.com (站点ID: zone-xxxxx) 的归属权。

Input: 

```
tccli teo VerifyOwnership --cli-unfold-argument  \
    --Domain example.com
```

Output: 
```
{
    "Response": {
        "Status": "fail",
        "Result": "解析 xx 得到 类型 xx 的内容 xx。\n 访问 http://xxx/.. 解析 xx 无法连接",
        "RequestId": "9kl50bew-89ga-44f4-91ce-78125d53vd2a"
    }
}
```

**Example 3: NS 接入时，查询 DNS 服务器是否切换成功**

验证 example.com 的 DNS 服务器是否已经切换成功。

Input: 

```
tccli teo VerifyOwnership --cli-unfold-argument  \
    --Domain example.com
```

Output: 
```
{
    "Response": {
        "Status": "fail",
        "Result": "当前域名的 DNS 服务器为 xxx，与预期服务器 xxx 不符合",
        "RequestId": "9kl50bew-89ga-44f4-91ce-78125d53vd2a"
    }
}
```

