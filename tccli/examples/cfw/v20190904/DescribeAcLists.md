**Example 1: ACl规则列表查询示例**

ACl规则列表查询示例

Input: 

```
tccli cfw DescribeAcLists --cli-unfold-argument  \
    --SearchValue {"common":"模糊检索"} \
    --Limit 1 \
    --Offset 0
```

Output: 
```
{
    "Response": {
        "AllTotal": 10,
        "Data": [
            {
                "AutoTask": "[{\"TaskId\":9070,\"TaskName\":\"aa\",\"LastTime\":\"\"}]",
                "City": 0,
                "CloudCode": "tencent",
                "Count": 0,
                "Country": 0,
                "Detail": "详情",
                "DstType": 1,
                "Id": 151973,
                "InstanceName": "andy的cvm",
                "Invalid": 0,
                "IsRegion": 0,
                "LogId": "datfaexd",
                "OrderIndex": 1,
                "Port": "-1/-1",
                "Protocol": "TCP",
                "RegName1": "广州",
                "RegName2": "新加坡",
                "SourceIp": "havip-0p99wbtb",
                "SrcType": 6,
                "Status": 1,
                "Strategy": 2,
                "TargetIp": "0.0.0.0/0",
                "Uuid": "1300448058_0.0.0.0/0_1730259837057017"
            }
        ],
        "Enable": 2,
        "RequestId": "e60361f4-8033-40ed-ab79-35f92fc50bf1",
        "Total": 10
    }
}
```

