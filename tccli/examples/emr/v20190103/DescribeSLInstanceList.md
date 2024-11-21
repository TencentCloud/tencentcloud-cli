**Example 1: Serverless HBase查询实例列表**

Serverless HBase查询实例列表

Input: 

```
tccli emr DescribeSLInstanceList --cli-unfold-argument  \
    --Offset 0 \
    --Limit 10 \
    --OrderField AddTime \
    --Asc 1 \
    --DisplayStrategy clusterList
```

Output: 
```
{
    "Response": {
        "InstancesList": [
            {
                "AddTime": "2024-03-14 17:40:19",
                "AppId": 251233704,
                "ClusterId": "emr-2ecolb9q",
                "ClusterName": "EMR-haosen",
                "Id": 126358006,
                "PayMode": 0,
                "RegionId": 1,
                "Status": 3,
                "StatusDesc": "集群生产中",
                "SubnetId": 2666622,
                "Tags": [],
                "VpcId": 11406751,
                "Zone": "ap-guangzhou-2",
                "ZoneId": 100002
            }
        ],
        "RequestId": "fde6361c-205a-45e5-8bec-34b9100fc5b0",
        "TotalCnt": 1
    }
}
```

