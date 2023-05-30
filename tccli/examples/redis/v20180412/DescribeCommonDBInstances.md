**Example 1: 请求示例**

废弃接口

Input: 

```
tccli redis DescribeCommonDBInstances --cli-unfold-argument  \
    --PayMode 0 \
    --InstanceIds crs-nh47ubwr
```

Output: 
```
{
    "Response": {
        "TotalCount": 0,
        "InstanceDetails": [
            {
                "InstanceName": "abc",
                "InstanceId": "abc",
                "AppId": 0,
                "ProjectId": 0,
                "Region": "abc",
                "Zone": "abc",
                "VpcId": "abc",
                "SubnetId": "abc",
                "Status": "abc",
                "Vips": [
                    "abc"
                ],
                "Vport": 0,
                "Createtime": "abc",
                "PayMode": 0,
                "NetType": 0
            }
        ],
        "RequestId": "abc"
    }
}
```

