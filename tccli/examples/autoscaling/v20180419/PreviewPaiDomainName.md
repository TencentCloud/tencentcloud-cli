**Example 1: 预览PAI实例域名**

预览PAI实例域名，返回一个可用于创建PAI实例的域名。

Input: 

```
tccli as PreviewPaiDomainName --cli-unfold-argument  \
    --DomainNameType tcb
```

Output: 
```
{
    "Response": {
        "DomainName": "salmonberry-ey5t3l0k.pai.tcloudbase.com",
        "RequestId": "cea75193-a9fb-4811-aa0b-b4d2096ef0d9"
    }
}
```

