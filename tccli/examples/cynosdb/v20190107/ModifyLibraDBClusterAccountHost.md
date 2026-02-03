**Example 1: 修改分析集群账号主机**



Input: 

```
tccli cynosdb ModifyLibraDBClusterAccountHost --cli-unfold-argument  \
    --ClusterId libradb-i794jfvg \
    --Account.AccountName admin \
    --Account.Host % \
    --NewHost 127.0.0.1
```

Output: 
```
{
    "Response": {
        "RequestId": "43272810-fd16-4ebb-9c3d-cd09d9969e53"
    }
}
```

