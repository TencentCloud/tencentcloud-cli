**Example 1: 创建域名示例**

创建域名示例

Input: 

```
tccli gaap CreateGlobalDomain --cli-unfold-argument  \
    --ProjectId 0 \
    --DefaultValue 127.0.0.1 \
    --Alias www.baidu.com
```

Output: 
```
{
    "Response": {
        "RequestId": "b4195a4c-7595-46db-b46d-7fcdafddee2c",
        "DomainId": "dm-bihtw7x3"
    }
}
```

