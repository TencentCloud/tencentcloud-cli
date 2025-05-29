**Example 1: 修改集群下载限制**



Input: 

```
tccli cynosdb ModifyBackupDownloadRestriction --cli-unfold-argument  \
    --ClusterIds cynosdbmysql-2p3wjmzt \
    --LimitType NoLimit \
    --VpcComparisonSymbol  \
    --IpComparisonSymbol 
```

Output: 
```
{
    "Response": {
        "RequestId": "1530aee8-5130-45ce-9f4e-dfb50a55e4d4"
    }
}
```

