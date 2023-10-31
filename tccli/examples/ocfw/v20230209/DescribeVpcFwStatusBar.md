**Example 1: DescribeVpcFwStatusBar 获取VPC防火墙状态栏数据**

DescribeVpcFwStatusBar 获取VPC防火墙状态栏数据

Input: 

```
tccli ocfw DescribeVpcFwStatusBar --cli-unfold-argument ```

Output: 
```
{
    "Response": {
        "FwBarStatus": {
            "BandWidthUsed": 5120,
            "DiffRegionFwInsId": "",
            "DiffRegionFwInsName": "",
            "DiffRegionMaxFlow": 0,
            "FwGroupId": "",
            "FwGroupMaxFlow": 0,
            "FwGroupName": "",
            "FwInsCount": 6,
            "FwInsId": "cfwew-7d50f9f5",
            "FwInsMaxFlow": 9028,
            "FwInsName": " [autotest][勿删]自动化测试",
            "FwSwitchCount": 5,
            "JoinInstanceCount": 13,
            "JoinVpcCntLimit": 10,
            "SameRegionFwInsId": "cfwew-7d50f9f5",
            "SameRegionFwInsName": " [autotest][勿删]自动化测试",
            "SameRegionMaxFlow": 9028,
            "VpcFwInsCntLimit": 11,
            "VpcRegionCntLimit": 5,
            "VpcThroughPut": 10240,
            "FwGroupCount": 1,
            "FwGroupMaxInsCount": 10,
            "InstanceQuota": 1
        },
        "RequestId": "c9343d64-31c1-482c-bbd9-5d74c177e1fb"
    }
}
```

