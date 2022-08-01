**Example 1: 根据域名删除转发规则**



Input: 

```
tccli gaap DeleteDomain --cli-unfold-argument  \
    --Domain a.a.com \
    --Force 1 \
    --ListenerId 0
```

Output: 
```
{
    "Response": {
        "RequestId": "c7bfcad5-3f20-472f-9afc-13a66faebad8"
    }
}
```

