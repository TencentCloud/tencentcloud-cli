**Example 1: 查询**

安灯工具查询指标数据

Input: 

```
tccli monitor DescribeAndonToolMetricData --cli-unfold-argument  \
    --Namespace abc \
    --ViewName abc \
    --Metric abc \
    --Period abc \
    --Dimension.0.Key abc \
    --Dimension.0.Value abc \
    --StartTime 0 \
    --EndTime 0
```

Output: 
```
{
    "Response": {
        "Period": "abc",
        "Metric": "abc",
        "StartTime": 0,
        "EndTime": 0,
        "Msg": "abc",
        "DataPoint": {
            "Dimension": [
                {
                    "Key": "abc",
                    "Value": "abc"
                }
            ],
            "Data": [
                {
                    "Timestamp": 0,
                    "Value": 0
                }
            ]
        },
        "RequestId": "abc"
    }
}
```

**Example 2: 测试环境真实查询**

测试环境真实查询

Input: 

```
tccli monitor DescribeAndonToolMetricData --cli-unfold-argument  \
    --Namespace qce/cvm \
    --ViewName cvm_device \
    --Metric cpu_usage \
    --Period 60 \
    --Dimension.0.Key vm_uuid \
    --Dimension.0.Value 5245b964-3c0b-4ff0-b108-179f94265be7 \
    --StartTime 1690952130 \
    --EndTime 1690952530
```

Output: 
```
{
    "Response": {
        "DataPoint": {
            "Data": [
                {
                    "Timestamp": 1690952160,
                    "Value": 1.4666700000000001
                },
                {
                    "Timestamp": 1690952220,
                    "Value": 1.3333300000000001
                },
                {
                    "Timestamp": 1690952280,
                    "Value": 1.6500000000000001
                },
                {
                    "Timestamp": 1690952340,
                    "Value": 1.4666700000000001
                },
                {
                    "Timestamp": 1690952400,
                    "Value": 1.9333300000000002
                },
                {
                    "Timestamp": 1690952460,
                    "Value": 1.6333300000000002
                },
                {
                    "Timestamp": 1690952520,
                    "Value": 1.5000000000000002
                }
            ],
            "Dimension": [
                {
                    "Key": "vm_uuid",
                    "Value": "5245b964-3c0b-4ff0-b108-179f94265be7"
                }
            ]
        },
        "EndTime": 1690952530,
        "Metric": "cpu_usage",
        "Msg": "Success",
        "NextToken": "",
        "Period": 60,
        "RequestId": "afa5f1c0-f060-4ef3-aa28-103aa7946a1e",
        "StartTime": 1690952130
    }
}
```

