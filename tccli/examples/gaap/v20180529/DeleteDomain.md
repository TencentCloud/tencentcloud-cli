**Example 1: 根据域名删除转发规则**



Input: 

```
tccli gaap DeleteDomain --cli-unfold-argument  \
    --Domain www.baidu.com \
    --Force 1 \
    --ListenerId listener-0s9kb7qt
```

Output: 
```
{
    "Response": {
        "RequestId": "c7bfcad5-3f20-472f-9afc-13a66faebad8"
    }
}
```

