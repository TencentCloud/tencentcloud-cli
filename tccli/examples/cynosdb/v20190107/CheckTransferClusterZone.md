**Example 1: 检查是否可以发起跨可用区迁移**



Input: 

```
tccli cynosdb CheckTransferClusterZone --cli-unfold-argument  \
    --ClusterId cynosdbmysql-86dzof1j \
    --DstZone ap-guangzhou-5
```

Output: 
```
{
    "Response": {
        "CheckStatus": true,
        "RequestId": "6febb6f0-b0fc-11ee-93cb-73a07daf38c5"
    }
}
```

