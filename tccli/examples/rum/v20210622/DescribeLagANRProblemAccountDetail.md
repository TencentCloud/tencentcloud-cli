**Example 1: 查询卡顿详情**

查询卡顿详情

Input: 

```
tccli rum DescribeLagANRProblemAccountDetail --cli-unfold-argument  \
    --ProductId 0dc5283a55 \
    --ClientIdentify B65E1949-C258-4E4A-9606-0DECEF483C71 \
    --Feature 50DFB3ACDC47C821EEA254947C238FF1 \
    --RequestHeader BEGIN{"X-ProductId": "0dc5283a55","X-Tc-Username": "cdx_test"}END
```

Output: 
```
{
    "Response": {
        "Code": 0,
        "Data": "{\"base_rsp\":{\"code\":0,\"msg\":\"success\"},\"account_detail\":null}",
        "Message": "",
        "RequestId": "a9a47b9b-947d-47b8-bafd-6db4ad607e23"
    }
}
```

