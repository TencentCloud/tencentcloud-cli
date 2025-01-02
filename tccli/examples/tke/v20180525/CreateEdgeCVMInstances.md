**Example 1: 创建边缘容器CVM机器**

创建边缘容器CVM机器

Input: 

```
tccli tke CreateEdgeCVMInstances --cli-unfold-argument  \
    --ClusterID cls-e55paxnt \
    --CvmRegion ap-guangzhou \
    --CvmCount 3 \
    --UserScript whoami \
    --RunInstancePara {"InstanceChargeType":"POSTPAID_BY_HOUR","Placement":{"Zone":"ap-guangzhou-3","ProjectId":0},"InstanceType":"S5.SMALL2","SystemDisk":{"DiskType":"CLOUD_BSSD","DiskSize":50},"VirtualPrivateCloud":{"VpcId":"vpc-e55paxnt","SubnetId":"subnet-e55paxnt","AsVpcGateway":false},"InternetAccessible":{"InternetChargeType":"TRAFFIC_POSTPAID_BY_HOUR","InternetMaxBandwidthOut":1,"PublicIpAssigned":true},"InstanceCount":1,"ImageId":"img-e55paxnt","InstanceName":"tkeedge_cls-e55paxnt_worker","LoginSettings":{"KeyIds":["skey-e55paxnt"]},"SecurityGroupIds":["sg-e55paxnt"],"EnhancedService":{"SecurityService":{"Enabled":true},"MonitorService":{"Enabled":true}}} \
    --EnableEni true
```

Output: 
```
{
    "Response": {
        "RequestId": "d40cdb72-7bc0-4b48-b3aa-25e8401f6999",
        "CvmIdSet": [
            "cvm-197252sp",
            "cvm-19725win",
            "cvm-19623ash"
        ]
    }
}
```

