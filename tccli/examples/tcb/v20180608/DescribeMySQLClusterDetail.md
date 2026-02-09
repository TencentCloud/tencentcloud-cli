**Example 1: DescribeMySqlClusterDetail**



Input: 

```
tccli tcb DescribeMySQLClusterDetail --cli-unfold-argument  \
    --EnvId *******p**-8g1j2dbc0df14561
```

Output: 
```
{
    "Response": {
        "Data": {
            "DbClusterId": "cynos*******-6gian***",
            "DbInfo": {
                "ClusterStatus": "running",
                "DbType": "MYSQL",
                "DbVersion": "5.7",
                "IsOpenPubNetAccess": false,
                "MaxCpu": 0.5,
                "MinCpu": 0.25,
                "ServerlessStatus": "pause",
                "Status": "running",
                "StorageLimit": 100000,
                "UsedStorage": 21000000,
                "WanStatus": "init"
            },
            "NetInfo": {
                "Net": "vpc-py8*****/subnet-68*****p",
                "PrivateNetAddress": "10*******3:3306",
                "PubNetAddress": "",
                "SubnetId": "subnet-68****d*",
                "SubnetName": "cloudbase_run_tdsqlc_subnet",
                "VpcId": "vpc-py******",
                "VpcName": "tcb_pre-**l*f*s**r*******q098a0434e"
            }
        },
        "RequestId": "72b253f4-a578-4940-8d99-cb417f26e286"
    }
}
```

