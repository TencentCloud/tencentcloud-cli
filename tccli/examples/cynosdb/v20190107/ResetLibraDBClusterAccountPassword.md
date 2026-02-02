**Example 1: 修改分析集群账号密码**



Input: 

```
tccli cynosdb ResetLibraDBClusterAccountPassword --cli-unfold-argument  \
    --ClusterId libradb-i8okw971 \
    --AccountPassword aQvlNPVkdtbh708 \
    --AccountName root
```

Output: 
```
{
    "Response": {
        "RequestId": "20f664c0-8d0d-4a4b-950b-3955c909b228"
    }
}
```

