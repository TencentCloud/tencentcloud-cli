**Example 1: ListCloudInstances**

查询云实例列表

Input: 

```
tccli wedata ListCloudInstances --cli-unfold-argument  \
    --ConnectionType TENCENT_MYSQL \
    --InstanceRegion ap-guangzhou
```

Output: 
```
{
    "Response": {
        "Data": {
            "Instances": [
                {
                    "InstanceId": "cdb-orkfayb3",
                    "InstanceName": "mlflow-251436191",
                    "InstanceRegion": "ap-guangzhou",
                    "InstanceRegionName": "",
                    "InstanceStatus": "1"
                }
            ]
        },
        "RequestId": "eafe5dc9-abd8-413a-8955-6f002bdf6956"
    }
}
```

