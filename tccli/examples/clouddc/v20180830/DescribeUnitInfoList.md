**Example 1: 根据组织id集合，批量获取组织信息**



Input: 

```
tccli clouddc DescribeUnitInfoList --cli-unfold-argument  \
    --UnitIds 44618
```

Output: 
```
{
    "Response": {
        "RequestId": "7bb3d465-7dac-458f-b253-b127feea9bdb",
        "JsonString": "[{\"unitId\":44618,\"unitName\":\"\\u57fa\\u7840\\u5e73\\u53f0\\u5f00\\u53d1\\u7ec4\",\"unitFullId\":\";0;29294;43898;44613;\",\"unitFullIdNew\":\";0;29294;43898;44613;44618;\",\"unitFullName\":\"CSIG\\u4e91\\u4e0e\\u667a\\u6167\\u4ea7\\u4e1a\\u4e8b\\u4e1a\\u7fa4\\/\\u4e1a\\u52a1\\u7ecf\\u8425\\u7ba1\\u7406\\u90e8\\/\\u6280\\u672f\\u7814\\u53d1\\u4e2d\\u5fc3\\/\\u57fa\\u7840\\u5e73\\u53f0\\u5f00\\u53d1\\u7ec4\",\"isVirtual\":0,\"unitStatus\":1,\"bg\":\"CSIG\\u4e91\\u4e0e\\u667a\\u6167\\u4ea7\\u4e1a\\u4e8b\\u4e1a\\u7fa4\",\"bgId\":29294,\"department\":\"\\u4e1a\\u52a1\\u7ecf\\u8425\\u7ba1\\u7406\\u90e8\",\"departmentId\":43898,\"center\":\"\\u6280\\u672f\\u7814\\u53d1\\u4e2d\\u5fc3\",\"centerId\":44613}]"
    }
}
```

