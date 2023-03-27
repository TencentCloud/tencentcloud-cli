**Example 1: 设置白板月功能费自动续费**



Input: 

```
tccli tiw ModifyAutoRenewFlag --cli-unfold-argument  \
    --SubProduct sp_tiw_package \
    --ResourceId sp_tiw_package-251006355-prepaid-1 \
    --AutoRenewFlag 1
```

Output: 
```
{
    "Response": {
        "RequestId": "d290f1ee-6c54-4b01-90e6-d701748f0851"
    }
}
```

