**Example 1: CheckIntegrationNodeNameExists**

判断集成节点名称是否存在

Input: 

```
tccli wedata CheckIntegrationNodeNameExists --cli-unfold-argument  \
    --ProjectId 11022568003970304 \
    --Id 0 \
    --TaskId 20220506145218687 \
    --Name hive
```

Output: 
```
{
    "Response": {
        "Data": true,
        "RequestId": "as1cs2c123asyi23bh213cc"
    }
}
```

