**Example 1: 添加诊断URL**



Input: 

```
tccli cdn CreateDiagnoseUrl --cli-unfold-argument  \
    --Url http://www.test.com/test.txt
```

Output: 
```
{
    "Response": {
        "RequestId": "b3eee570-0d5f-46b2-89a3-160f4e654eaf",
        "DiagnoseLink": "http://cdn.cloud.tencent.com/self_diagnose/a49ecccd"
    }
}
```

