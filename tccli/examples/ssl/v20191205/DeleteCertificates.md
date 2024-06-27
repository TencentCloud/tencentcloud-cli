**Example 1: 批量删除**

批量删除

Input: 

```
tccli ssl DeleteCertificates --cli-unfold-argument ```

Output: 
```
{
    "Response": {
        "CertTaskIds": [
            {
                "CertId": "1ODjBeH8",
                "TaskId": "1"
            },
            {
                "CertId": "25EMBPYQ",
                "TaskId": "2"
            },
            {
                "CertId": "txV0pewo",
                "TaskId": "3"
            },
            {
                "CertId": "rcGiGyTx",
                "TaskId": "4"
            },
            {
                "CertId": "4FVmnb1u",
                "TaskId": "5"
            }
        ],
        "Success": [],
        "Fail": [],
        "RequestId": "687f27b0-c256-40ea-adf6-efb715001f2e"
    }
}
```

