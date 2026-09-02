**Example 1: 按实例 ID 精确查询**



Input: 

```
tccli tdmq DescribePulsarProInstances --cli-unfold-argument  \
    --Filters.0.Name instanceIds \
    --Filters.0.Values pulsar-aer8pde2z2we \
    --Limit 10 \
    --Offset 0
```

Output: 
```
{
    "Response": {
        "TotalCount": 1,
        "Instances": [
            {
                "InstanceId": "pulsar-aer8pde2z2we",
                "InstanceName": "DevName",
                "InstanceVersion": "2.9.1",
                "Status": 1,
                "ConfigDisplay": "基础型",
                "MaxTps": 1000,
                "MaxStorage": 0,
                "ExpireTime": 1735689600000,
                "AutoRenewFlag": 1,
                "PayMode": 1,
                "Remark": "devRemark",
                "SpecName": "PULSAR.P2.MINI1",
                "ScalableTps": 0,
                "VpcId": "vpc-xxxx",
                "SubnetId": "subnet-xxxx",
                "MaxBandWidth": 40,
                "Tags": [
                    {
                        "TagKey": "devKey",
                        "TagValue": "devValue"
                    }
                ],
                "CreateTime": "2023-12-08 10:25:51",
                "BillingLabelVersion": "PULSAR.P2"
            }
        ],
        "RequestId": "e83dfdba-ed1a-4460-b175-81430ddf61fa"
    }
}
```

**Example 2: 按集群名称模糊查询**



Input: 

```
tccli tdmq DescribePulsarProInstances --cli-unfold-argument  \
    --Filters.0.Name instanceName \
    --Filters.0.Values DevName \
    --Limit 10 \
    --Offset 0
```

Output: 
```
{
    "Response": {
        "TotalCount": 1,
        "Instances": [
            {
                "InstanceId": "pulsar-aer8pde2z2we",
                "InstanceName": "DevName",
                "InstanceVersion": "2.9.1",
                "Status": 1,
                "ConfigDisplay": "基础型",
                "MaxTps": 1000,
                "MaxStorage": 0,
                "ExpireTime": 1735689600000,
                "AutoRenewFlag": 1,
                "PayMode": 1,
                "Remark": "devRemark",
                "SpecName": "PULSAR.P2.MINI1",
                "ScalableTps": 0,
                "VpcId": "vpc-xxxx",
                "SubnetId": "subnet-xxxx",
                "MaxBandWidth": 40,
                "Tags": [
                    {
                        "TagKey": "devKey",
                        "TagValue": "devValue"
                    }
                ],
                "CreateTime": "2023-12-08 10:25:51",
                "BillingLabelVersion": "PULSAR.P2"
            }
        ],
        "RequestId": "f94eab12-3c5d-4a8e-9b12-7d6e8f9a0b1c"
    }
}
```

**Example 3: 按集群状态查询（仅查健康状态）**



Input: 

```
tccli tdmq DescribePulsarProInstances --cli-unfold-argument  \
    --Filters.0.Name status \
    --Filters.0.Values 1 \
    --Limit 10 \
    --Offset 0
```

Output: 
```
{
    "Response": {
        "TotalCount": 2,
        "Instances": [
            {
                "InstanceId": "pulsar-aer8pde2z2we",
                "InstanceName": "DevName",
                "InstanceVersion": "2.9.1",
                "Status": 1,
                "ConfigDisplay": "基础型",
                "MaxTps": 1000,
                "MaxStorage": 0,
                "ExpireTime": 1735689600000,
                "AutoRenewFlag": 1,
                "PayMode": 1,
                "Remark": "devRemark",
                "SpecName": "PULSAR.P2.MINI1",
                "ScalableTps": 0,
                "VpcId": "vpc-xxxx",
                "SubnetId": "subnet-xxxx",
                "MaxBandWidth": 40,
                "Tags": [
                    {
                        "TagKey": "devKey",
                        "TagValue": "devValue"
                    }
                ],
                "CreateTime": "2023-12-08 10:25:51",
                "BillingLabelVersion": "PULSAR.P2"
            }
        ],
        "RequestId": "d4e5f6a7-b8c9-0123-4567-89abcdef0123"
    }
}
```

**Example 4: 按集群类型查询（仅查标准版 S2）**

P1 或 PULSAR.P1：固定存储专业版
P2 或 PULSAR.P2：弹性存储专业版
S2 或 PULSAR.S2：标准版

Input: 

```
tccli tdmq DescribePulsarProInstances --cli-unfold-argument  \
    --Filters.0.Name clusterType \
    --Filters.0.Values S2 \
    --Limit 10 \
    --Offset 0
```

Output: 
```
{
    "Response": {
        "TotalCount": 1,
        "Instances": [
            {
                "InstanceId": "pulsar-bx9f3kd7m4np",
                "InstanceName": "standard-test-01",
                "InstanceVersion": "3.0.0",
                "Status": 1,
                "ConfigDisplay": "标准型",
                "MaxTps": 1000,
                "MaxStorage": 0,
                "ExpireTime": 1735689600000,
                "AutoRenewFlag": 0,
                "PayMode": 1,
                "Remark": "",
                "SpecName": "PULSAR.S2.MINI1",
                "ScalableTps": 0,
                "VpcId": "vpc-yyyy",
                "SubnetId": "subnet-yyyy",
                "MaxBandWidth": 20,
                "Tags": [],
                "CreateTime": "2026-08-01 14:30:00",
                "BillingLabelVersion": "PULSAR.S2"
            }
        ],
        "RequestId": "a1b2c3d4-e5f6-7890-abcd-ef1234567890"
    }
}
```

**Example 5: 组合过滤（按集群类型 + 实例名称）**



Input: 

```
tccli tdmq DescribePulsarProInstances --cli-unfold-argument  \
    --Filters.0.Name clusterType \
    --Filters.0.Values S2 \
    --Filters.1.Name instanceName \
    --Filters.1.Values dev \
    --Limit 20 \
    --Offset 0
```

Output: 
```
{
    "Response": {
        "TotalCount": 1,
        "Instances": [
            {
                "InstanceId": "pulsar-bx9f3kd7m4np",
                "InstanceName": "standard-dev-01",
                "InstanceVersion": "3.0.0",
                "Status": 1,
                "ConfigDisplay": "标准型",
                "MaxTps": 1000,
                "MaxStorage": 0,
                "ExpireTime": 1735689600000,
                "AutoRenewFlag": 0,
                "PayMode": 1,
                "Remark": "",
                "SpecName": "PULSAR.S2.MINI1",
                "ScalableTps": 0,
                "VpcId": "vpc-yyyy",
                "SubnetId": "subnet-yyyy",
                "MaxBandWidth": 20,
                "Tags": [],
                "CreateTime": "2026-08-01 14:30:00",
                "BillingLabelVersion": "PULSAR.S2"
            }
        ],
        "RequestId": "12345678-abcd-ef01-2345-6789abcdef01"
    }
}
```

