**Example 1: 将一个成员添加到团队**



Input: 

```
tccli cme AddTeamMember --cli-unfold-argument  \
    --Platform test \
    --TeamId 1kdk882ddd88338ddd3k3 \
    --TeamMembers.0.Remark 编辑张三 \
    --TeamMembers.0.MemberId 1kd3ej3okjdije3lejjdjk99
```

Output: 
```
{
    "Response": {
        "RequestId": "99004d9f-aeec-4817-bbe2-d3499f95a2bf"
    }
}
```

