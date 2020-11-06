**Example 1: 查询所支持的实例机型族信息**

查询广州地域的实例机型组信息。

Input: 

```
tccli cvm DescribeInstanceFamilyConfigs --cli-unfold-argument  \
    --Region ap-guangzhou
```

Output: 
```
{
    "Response": {
        "InstanceFamilyConfigSet": [
            {
                "InstanceFamilyName": "标准型S1",
                "InstanceFamily": "S1"
            },
            {
                "InstanceFamilyName": "网络优化型N1",
                "InstanceFamily": "N1"
            },
            {
                "InstanceFamilyName": "高IO型I1",
                "InstanceFamily": "I1"
            },
            {
                "InstanceFamilyName": "内存型M1",
                "InstanceFamily": "M1"
            },
            {
                "InstanceFamilyName": "标准型S2",
                "InstanceFamily": "S2"
            },
            {
                "InstanceFamilyName": "标准型SN2",
                "InstanceFamily": "SN2"
            },
            {
                "InstanceFamilyName": "高IO型I2",
                "InstanceFamily": "I2"
            },
            {
                "InstanceFamilyName": "内存型M2",
                "InstanceFamily": "M2"
            },
            {
                "InstanceFamilyName": "计算型C2",
                "InstanceFamily": "C2"
            },
            {
                "InstanceFamilyName": "计算型CN2",
                "InstanceFamily": "CN2"
            },
            {
                "InstanceFamilyName": "标准型S3",
                "InstanceFamily": "S3"
            },
            {
                "InstanceFamilyName": "计算型C3",
                "InstanceFamily": "C3"
            },
            {
                "InstanceFamilyName": "FPGA型FX2",
                "InstanceFamily": "FX2"
            },
            {
                "InstanceFamilyName": "GPU计算型GN2",
                "InstanceFamily": "GN2"
            },
            {
                "InstanceFamilyName": "GPU渲染型GA2",
                "InstanceFamily": "GA2"
            },
            {
                "InstanceFamilyName": "GPU计算型GN8",
                "InstanceFamily": "GN8"
            },
            {
                "InstanceFamilyName": "独享型",
                "InstanceFamily": "CDH"
            },
            {
                "InstanceFamilyName": "共享核",
                "InstanceFamily": "SHARED"
            },
            {
                "InstanceFamilyName": "特殊机型",
                "InstanceFamily": "SPECIAL"
            },
            {
                "InstanceFamilyName": "其他",
                "InstanceFamily": "OTHER"
            }
        ],
        "RequestId": "b061782b-934a-4e53-b1eb-d5f2fed8130e"
    }
}
```

