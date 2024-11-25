**Example 1: 查询防火墙(组)ID名称及实例下对应关系**

查询防火墙(组)ID名称及实例下对应关系

Input: 

```
tccli cfw DescribeVpcFwGroupIns --cli-unfold-argument ```

Output: 
```
{
    "Response": {
        "FwGroupLst": [
            {
                "FwGroupId": "cfwg-wxecrvtb",
                "FwGroupName": "防火墙1",
                "FwInstanceLst": [
                    {
                        "FwInsId": "cfwew-wxecrvtb",
                        "FwInsName": "实例1",
                        "FwInsRegion": "ap-guangzhou"
                    }
                ]
            }
        ],
        "RequestId": "0ea42a70-369b-407e-91e1-ca2d3b0b76b3"
    }
}
```

