**Example 1: 变更规格**

变更实例的内存配置

Input: 

```
tccli redis UpgradeInstance --cli-unfold-argument  \
    --InstanceId crs-5qlr**** \
    --MemSize 4096
```

Output: 
```
{
    "Response": {
        "DealName": "20250825297021509398751",
        "RequestId": "4daddc97-0005-45d8-b5b8-38514ec1e97c"
    }
}
```

