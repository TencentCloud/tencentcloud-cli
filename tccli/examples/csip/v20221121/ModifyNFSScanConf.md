**Example 1: 新增或更新NFS扫描全局配置**

新增或更新NFS扫描全局配置

Input: 

```
tccli csip ModifyNFSScanConf --cli-unfold-argument  \
    --Enable 1 \
    --Scope 1 \
    --Id 1 \
    --IncludeQuuid 3913529d-2d2c-485a-b07b-384f28781452 \
    --ExcludeQuuid 3913529d-2d2c-485a-b07b-384f28781452
```

Output: 
```
{
    "Response": {
        "RequestId": "c38104ae-20dc-473c-8e47-8a8bbe09ce97"
    }
}
```

