**Example 1: 修改分析集群账号描述**



Input: 

```
tccli cynosdb ModifyLibraDBClusterAccountDescription --cli-unfold-argument  \
    --ClusterId libradb-i794jfvg \
    --AccountName admin \
    --Host 127.0.0.1 \
    --Description 管理员
```

Output: 
```
{
    "Response": {
        "RequestId": "80a96cb7-85f0-4949-bf7f-4d359791abd3"
    }
}
```

