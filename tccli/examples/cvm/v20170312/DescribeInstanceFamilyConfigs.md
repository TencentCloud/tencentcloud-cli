**Example 1: Querying supported instance model families**

This example shows you how to query the list of instance model families supported in the Guangzhou region.

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
                "InstanceFamilyName": "Standard S1",
                "InstanceFamily": "S1"
            },
            {
                "InstanceFamilyName": "Network-optimized N1",
                "InstanceFamily": "N1"
            },
            {
                "InstanceFamilyName": "High IO I1",
                "InstanceFamily": "I1"
            },
            {
                "InstanceFamilyName": "MEM-optimized M1",
                "InstanceFamily": "M1"
            },
            {
                "InstanceFamilyName": "Standard S2",
                "InstanceFamily": "S2"
            },
            {
                "InstanceFamilyName": "Standard SN2",
                "InstanceFamily": "SN2"
            },
            {
                "InstanceFamilyName": "High IO I2",
                "InstanceFamily": "I2"
            },
            {
                "InstanceFamilyName": "MEM-optimized M2",
                "InstanceFamily": "M2"
            },
            {
                "InstanceFamilyName": "Compute C2",
                "InstanceFamily": "C2"
            },
            {
                "InstanceFamilyName": "Compute CN2",
                "InstanceFamily": "CN2"
            },
            {
                "InstanceFamilyName": "Standard S3",
                "InstanceFamily": "S3"
            },
            {
                "InstanceFamilyName": "Compute C3",
                "InstanceFamily": "C3"
            },
            {
                "InstanceFamilyName": "FPGA FX2",
                "InstanceFamily": "FX2"
            },
            {
                "InstanceFamilyName": "GPU compute GN2",
                "InstanceFamily": "GN2"
            },
            {
                "InstanceFamilyName": "GPU rendering GA2",
                "InstanceFamily": "GA2"
            },
            {
                "InstanceFamilyName": "GPU compute GN8",
                "InstanceFamily": "GN8"
            },
            {
                "InstanceFamilyName": "Dedicated",
                "InstanceFamily": "CDH"
            },
            {
                "InstanceFamilyName": "Shared core",
                "InstanceFamily": "SHARED"
            },
            {
                "InstanceFamilyName": "Special models",
                "InstanceFamily": "SPECIAL"
            },
            {
                "InstanceFamilyName": "Others",
                "InstanceFamily": "OTHER"
            }
        ],
        "RequestId": "b061782b-934a-4e53-b1eb-d5f2fed8130e"
    }
}
```

