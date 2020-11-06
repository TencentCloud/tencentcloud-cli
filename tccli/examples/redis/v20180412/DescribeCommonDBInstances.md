**Example 1: 请求示例**



Input: 

```
tccli redis DescribeCommonDBInstances --cli-unfold-argument  \
    --PayMode 0 \
    --InstanceIds ["crs-nh47ubwr"]
```

Output: 
```
{
    "Response": {
        "InstanceDetails": [
            {
                "AppId": 251006366,
                "Createtime": "2020-05-06 19:38:19",
                "InstanceId": "crs-nh47ubwr",
                "InstanceName": "crs-nh47ubwr",
                "NetType": 1,
                "PayMode": 1,
                "ProjectId": 1075668,
                "Region": "ap-guangzhou",
                "Status": "1",
                "SubnetId": 1210162,
                "Vips": [
                    "172.16.1.84"
                ],
                "VpcId": "79963",
                "Vport": 6379,
                "Zone": ""
            }
        ],
        "RequestId": "e306be36-f01b-477a-bdfb-e63d9b16d0a5",
        "TotalCount": 1
    }
}
```

