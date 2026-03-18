**Example 1: 删除保险箱**



Input: 

```
tccli cynosdb DeleteVaults --cli-unfold-argument  \
    --VaultIds vault-b63cedd8-1574-4390-89b5-6e703ef33e25
```

Output: 
```
{
    "Response": {
        "VaultTask": [
            {
                "TaskId": 4295131368,
                "VaultId": "vault-b63cedd8-1574-4390-89b5-6e703ef33e25"
            }
        ],
        "RequestId": "6619b3c9-0c5d-402a-bac5-fc0f6f7617e2"
    }
}
```

