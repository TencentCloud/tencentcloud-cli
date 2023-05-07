**Example 1: 更改某一条规则**

关闭白名单规则

Input: 

```
tccli waf ModifyDomainWhiteRule --cli-unfold-argument  \
    --Domain abc.qcloudwaf.com \
    --Id 111 \
    --Rules 2 \
    --Url /aa \
    --Function suffix \
    --Status 0
```

Output: 
```
{
    "Response": {
        "RequestId": "123894afsa90577"
    }
}
```

