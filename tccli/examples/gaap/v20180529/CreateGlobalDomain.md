**Example 1: 创建域名**

创建域名

Input: 

```
tccli gaap CreateGlobalDomain --cli-unfold-argument  \
    --ProjectId 0 \
    --DefaultValue 1.1.1.1 \
    --Alias test
```

Output: 
```
{
    "Response": {
        "DomainId": "dm-pcp5xac5",
        "RequestId": "0266e1f0-10a4-46ce-a118-29e360c90a1b"
    }
}
```

**Example 2: 创建域名示例**

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

