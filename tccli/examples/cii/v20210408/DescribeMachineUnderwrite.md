**Example 1: 查询机器核保任务数据示例**



Input: 

```
tccli cii DescribeMachineUnderwrite --cli-unfold-argument  \
    --UnderwriteTaskId 3456234
```

Output: 
```
{
    "Response": {
        "SubAccountUin": "xx",
        "Status": 0,
        "RequestId": "xx",
        "Uin": "xx",
        "UnderwriteResults": [
            {
                "CustomerId": "xx",
                "CustomerName": "xx",
                "Results": [
                    {
                        "InsuranceType": "xx",
                        "Result": [
                            {
                                "Laboratory": [
                                    {
                                        "Name": "xx",
                                        "Value": "xx",
                                        "Result": "xx"
                                    }
                                ],
                                "Explanation": [
                                    {
                                        "Name": "xx",
                                        "Value": "xx",
                                        "Result": "xx"
                                    }
                                ],
                                "Conclusion": "xx",
                                "Disease": [
                                    {
                                        "Name": "xx",
                                        "Value": "xx",
                                        "Result": "xx"
                                    }
                                ],
                                "Title": "xx"
                            }
                        ]
                    }
                ]
            }
        ],
        "PolicyId": "xx",
        "MainTaskId": "xx",
        "UnderwriteTaskId": "xx"
    }
}
```

