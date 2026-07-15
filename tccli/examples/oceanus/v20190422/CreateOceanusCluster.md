**Example 1: 创建Oceanus集群**

创建Oceanus集群

Input: 

```
tccli oceanus CreateOceanusCluster --cli-unfold-argument  \
    --ClusterName *****_cluster \
    --RegionId 1 \
    --ZoneId 100002 \
    --CU 12 \
    --LoginPassword ********* \
    --VpcDescriptions.0.VpcId vpc-cp****** \
    --VpcDescriptions.0.SubnetId subnet-5b****** \
    --DefaultCOSBucket autotest-************* \
    --InstanceChargeType PREPAID \
    --Remark create_cluster \
    --Period 1 \
    --RenewFlag NOTIFY_AND_MANUAL_RENEW \
    --FlinkWebUINetworkAccessType NetworkAccess_EXTERNAL
```

Output: 
```
{
    "Response": {
        "ClusterId": "cluster-********",
        "RequestId": "fc61dd48-34a6-4ed1-832f-e515c39756a0"
    }
}
```

