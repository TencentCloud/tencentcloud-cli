**Example 1: 请求示例**

废弃接口

Input: 

```
tccli redis DescribeCommonDBInstances --cli-unfold-argument  \
    --PayMode 0 \
    --InstanceIds crs-xjhsdj****
```

Output: 
```
{
    "Response": {
        "TotalCount": 0,
        "InstanceDetails": [
            {
                "AppId": 1251111111,
                "Createtime": "2022-06-13 21:41:40",
                "InstanceId": "crs-xjhsdj****",
                "InstanceName": "dba-stag",
                "NetType": 1,
                "PayMode": 1,
                "ProjectId": 0,
                "Region": "ap-beijing",
                "Status": "2",
                "SubnetId": "unknown-unSubnetId",
                "Vips": [
                    "10.76.128.10"
                ],
                "VpcId": "unknown-unVpcId",
                "Vport": 6379,
                "Zone": "ap-beijing-1"
            }
        ],
        "RequestId": "fc4a37f4-b27d-4aaf-9661-8212c9dabmclnvXXX"
    }
}
```

