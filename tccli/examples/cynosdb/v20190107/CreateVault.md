**Example 1: 创建保险箱**



Input: 

```
tccli cynosdb CreateVault --cli-unfold-argument  \
    --VaultName dylaa_test \
    --BackupSaveSeconds 1 \
    --KeyRegion ap-guangzhou
```

Output: 
```
{
    "Response": {
        "TaskId": 4295117983,
        "RequestId": "f15e9603-50b4-4e77-9388-5031d4ca2508"
    }
}
```

