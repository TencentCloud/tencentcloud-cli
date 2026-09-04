**Example 1: 校验specName是否有重名**



Input: 

```
tccli dlc CheckJobSpecName --cli-unfold-argument  \
    --SpecName aiidany
```

Output: 
```
{
    "Response": {
        "Available": false,
        "Reason": "配置名称 'aiidany' 在当前应用下已存在，请使用其他名称",
        "RequestId": "ceb60424-cf0d-4fb3-a884-a84b106eaa52"
    }
}
```

