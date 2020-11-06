**Example 1: 新增/修改本地提权规则**

新增/修改本地提权规则

Input: 

```
tccli yunjing EditPrivilegeRule --cli-unfold-argument  \
    --ProcessName bash \
    --HostIp 127.0.0.1 \
    --SMode 1
```

Output: 
```
{
    "Response": {
        "RequestId": "354f4ac3-8546-4516-8c8a-69e3ab73aa8a"
    }
}
```

