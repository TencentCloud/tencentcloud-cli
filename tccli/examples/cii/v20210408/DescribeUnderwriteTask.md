**Example 1: 查询核保任务数据示例**



Input: 

```
tccli cii DescribeUnderwriteTask --cli-unfold-argument  \
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
                "ManualDetail": [
                    {
                        "Explanation": "xx",
                        "Type": "xx",
                        "Conclusion": "xx"
                    }
                ],
                "ReviewTime": "xx",
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
                ],
                "CustomerName": "xx",
                "CustomerId": "xx"
            }
        ],
        "PolicyId": "xx",
        "MainTaskId": "xx",
        "UnderwriteTaskId": "xx"
    }
}
```

