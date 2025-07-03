**Example 1: 配置组配置参数信息**



Input: 

```
tccli emr DescribeServiceConfGroupInfos --cli-unfold-argument  \
    --InstanceId emr-cp4f67tz \
    --ServiceName HDFS \
    --ConfGroupName hdfs-core-defaultGroup \
    --PageNo 1 \
    --PageSize 10
```

Output: 
```
{
    "Response": {
        "ConfItemKVList": [
            {
                "InFile": "core-site.xml",
                "Name": "ZGVsZWdhdGlvbi50b2tlbi5pZGVudGlmaWVyLnNlcmlhbGl6YXRpb24udmVyc2lvbg==",
                "Value": "MA=="
            },
            {
                "InFile": "core-site.xml",
                "Name": "ZGVsZWdhdGlvbi50b2tlbi5pZGVudGlmaWVyLnRyYW5zbWlzc2lvbi52ZXJzaW9u",
                "Value": "MA=="
            },
            {
                "InFile": "core-site.xml",
                "Name": "ZW1yLmNmcy5ncm91cC5pZC5tYXA=",
                "Value": "cm9vdDowO2hhZG9vcDo1MDA="
            },
            {
                "InFile": "core-site.xml",
                "Name": "ZW1yLmNmcy5pby5ibG9ja3NpemU=",
                "Value": "MTA0ODU3Ng=="
            },
            {
                "InFile": "core-site.xml",
                "Name": "ZW1yLmNmcy51c2VyLmlkLm1hcA==",
                "Value": "cm9vdDowO2hhZG9vcDo1MDA="
            },
            {
                "InFile": "core-site.xml",
                "Name": "ZW1yLmNmcy53cml0ZS5sZXZlbA==",
                "Value": "Mg=="
            },
            {
                "InFile": "core-site.xml",
                "Name": "ZW1yLnRlbXJmcy5kb3dubG9hZC5tZDU=",
                "Value": "NTNiNGY5NWQxYzQ0YTI2OGYxNmIwMDllNDNkYjcxMzA="
            },
            {
                "InFile": "core-site.xml",
                "Name": "ZW1yLnRlbXJmcy5kb3dubG9hZC5yZWdpb24=",
                "Value": "Z3o="
            },
            {
                "InFile": "core-site.xml",
                "Name": "ZW1yLnRlbXJmcy5kb3dubG9hZC52ZXJzaW9u",
                "Value": "My4xLjAtOC4yLjctMS4wLjg="
            },
            {
                "InFile": "core-site.xml",
                "Name": "ZW1yLnRlbXJmcy50bXAuY2FjaGUuZGly",
                "Value": "L2RhdGEvZW1yL2hkZnMvdG1wL3RlbXJmcw=="
            }
        ],
        "RequestId": "d2d5d132-d5f9-4b76-90b3-a12756be5d92",
        "TotalCount": 146
    }
}
```

