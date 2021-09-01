**Example 1: 存证基本信息查询**

用户通过存证编码向BTOE查询存证基本信息。

Input: 

```
tccli btoe GetDepositInfo --cli-unfold-argument  \
    --EvidenceId 存证编码
```

Output: 
```
{
    "Response": {
        "RequestId": "testt222e32278733387121ststtest",
        "EvidenceId": "testt222e32278733387121ststtest",
        "EvidenceTime": "2021-03-26 09:06:05",
        "EvidenceTxHash": "0x7a0448ff9dd3bb1aa74534a7384b6515d715dc8aa26b68449ce8a6d6b6b5cec3"
    }
}
```

