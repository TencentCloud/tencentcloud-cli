**Example 1: 实例规格映射**

实例规格映射

Input: 

```
tccli cynosdb SwitchSpec --cli-unfold-argument  \
    --Cpu 1 \
    --Memory 1
```

Output: 
```
{
    "Response": {
        "Cpu": 1,
        "Mem": 1,
        "StorageLimit": 3000,
        "RequestId": "abc"
    }
}
```

