**Example 1: 修改媒体名称**

 

Input: 

```
tccli cme ModifyMaterial --cli-unfold-argument  \
    --Platform test \
    --MaterialId 5fd8ad3d628dc30001bd0895 \
    --Name 修改媒体名称
```

Output: 
```
{
    "Response": {
        "RequestId": "7bf08361-4455-4cbd-afd6-423b62c54a05"
    }
}
```

**Example 2: 修改媒体的分类**

 

Input: 

```
tccli cme ModifyMaterial --cli-unfold-argument  \
    --Platform test \
    --MaterialId 5fd8ad3d628dc30001bd0895 \
    --ClassPath /媒体/视频
```

Output: 
```
{
    "Response": {
        "RequestId": "7bf08361-4455-4cbd-afd6-423b62c54a12"
    }
}
```

**Example 3: 修改媒体归属为团队**

 

Input: 

```
tccli cme ModifyMaterial --cli-unfold-argument  \
    --Platform test \
    --MaterialId 5fd8ad3d628dc30001bd0895 \
    --Owner.Id cmetid_acbde8ad3do0303dc1b33 \
    --Owner.Type TEAM
```

Output: 
```
{
    "Response": {
        "RequestId": "7bf08361-4455-4cbd-afd6-423b62c54a09"
    }
}
```

