**Example 1: 调用示例**



Input: 

```
tccli ai3d DescribeHunyuanTo3DMotionJob --cli-unfold-argument  \
    --JobId 1439092349727752192
```

Output: 
```
{
    "Response": {
        "ErrorCode": "",
        "ErrorMessage": "",
        "ResultFile3Ds": [
            {
                "Type": "FBX",
                "Url": "https://*******************.cos.ap-guangzhou.tencentcos.cn/text2motion/output/251202827/cfb02f90-e884-415d-8dcd-60cc7e1503de_output.fbx?q-sign-algorithm=sha1&q-ak=************************************&q-sign-time=1777001423%3B1777087822&q-key-time=1777001423%3B1777087822&q-header-list=host&q-url-param-list=&q-signature=54bba445ebf011e4b3f07147f0184f3623a87350"
            }
        ],
        "Status": "DONE",
        "RequestId": "578477b2-29ad-4226-b883-cdd04059e0ac"
    }
}
```

