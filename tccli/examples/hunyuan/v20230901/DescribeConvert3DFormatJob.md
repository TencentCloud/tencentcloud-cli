**Example 1: 调用示例**



Input: 

```
tccli hunyuan DescribeConvert3DFormatJob --cli-unfold-argument  \
    --JobId 1433027947910201344
```

Output: 
```
{
    "Response": {
        "ErrorCode": "",
        "ErrorMessage": "",
        "ResultFile3Ds": [
            {
                "Type": "OBJ",
                "Url": "https://**************************.cos.ap-singapore.tencentcos.cn/3d/output/251292921/ef328ce7-034a-4f15-90e9-bde060a38865_output.obj?q-sign-algorithm=sha1&q-ak=************************************&q-sign-time=1775554903%3B1775641302&q-key-time=1775554903%3B1775641302&q-header-list=host&q-url-param-list=&q-signature=4553d0ec3cb72720254cd3820cfaccddfde651af"
            }
        ],
        "Status": "DONE",
        "RequestId": "e5b79dfe-c1a9-4527-81e6-a82b76cf7315"
    }
}
```

