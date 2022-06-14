**Example 1: 查询基础诊断资源使用情况**

查询当前用户的基础诊断资源使用情况

Input: 

```
tccli mmps DescribeBasicDiagnosisResourceUsageInfo --cli-unfold-argument  \
    --Mode 1
```

Output: 
```
{
    "Response": {
        "RequestId": "5e93a212-ca01-0fdc-eedd-5a1fce5e83e6",
        "Ret": 0,
        "ResourceName": "sv_mps_safety_diagnosis_basic_diagnosis",
        "Total": 10,
        "UnusedCount": 5
    }
}
```

