**Example 1: 创建一个团队**



Input: 

```
tccli cme CreateTeam --cli-unfold-argument  \
    --Platform test \
    --Name 测试团队名称 \
    --OwnerRemark 管理员李四 \
    --OwnerId 997988688
```

Output: 
```
{
    "Response": {
        "TeamId": "cmetid_19882998399iieii87neu78",
        "RequestId": "99004d9f-aeec-4817-bbe2-d3499f95a2bf"
    }
}
```

