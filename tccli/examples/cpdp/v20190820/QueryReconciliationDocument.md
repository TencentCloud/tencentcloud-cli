**Example 1: 查询对账文件信息**



Input: 

```
tccli cpdp QueryReconciliationDocument --cli-unfold-argument  \
    --Placement.Zone ap-guangzhou-2 \
    --ImageId img-pmqg1cw7 \
    --MrchCode 1234 \
    --FileType CZ \
    --FileDate 20191018
```

Output: 
```
{
    "Response": {
        "TranItemArray": [
            {
                "FilePath": "/ejzb/1234/12345678910.txt.enc",
                "RandomPassword": "12345678910",
                "FileName": "CZ201910183691.ok.enc",
                "DrawCode": "96fbef7e-109c-4a08-a58e-7f556fb00d30"
            }
        ],
        "TxnReturnCode": "000000",
        "RequestId": "a39ac57e-17cd-4c7d-80c6-6e9a59b616f0",
        "ResultNum": "1",
        "TxnReturnMsg": "交易成功",
        "ReservedMsg": "",
        "CnsmrSeqNo": "U862831911061573032178"
    }
}
```

