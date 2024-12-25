**Example 1: 查询统一集群下实例ID列表**

查询统一集群下实例ID列表

Input: 

```
tccli cynosdb DescribeInstancesWithinSameCluster --cli-unfold-argument  \
    --UniqVpcId vpc-gy34u12n \
    --Vip 172.1.1.1
```

Output: 
```
{
    "Response": {
        "TotalCount": 1,
        "InstanceIds": [
            "cynosdbmysql-ins-pgbpxt11"
        ],
        "RequestId": "51169b54-61d4-4604-a07e-e519a5527923"
    }
}
```

