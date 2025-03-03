**Example 1: GetCosToken 示例**

开发空间-获取cos token

Input: 

```
tccli wedata GetCosToken --cli-unfold-argument  \
    --ProjectId 1470547050521227264 \
    --OriginDomain https://wedata-studio-dev.cloud.tencent.com \
    --CrossFlag True \
    --RemotePath /datastudio/project/1470547050521227264/00leo/testjiek/testpython1_20250227112840742605.py
```

Output: 
```
{
    "Response": {
        "Bucket": "wedata-fusion-dev-1257305158",
        "EndPoint": "",
        "Region": "ap-nanjing",
        "RequestId": "b696ccf1-7365-4fb1-b185-bfb642919d21",
        "Token": {
            "CreateTime": 1740711197,
            "ExpiredTime": 1740718397,
            "Id": null,
            "OperatorUin": null,
            "OwnerUin": null,
            "Response": null,
            "SecretId": "AKID876VJThK494g_G9oRIqcL5Oy0kvWLB8uLJY7zmGYW55npHno3TdFo5mEMHCwcYFy",
            "SecretKey": "tOBaGJEmLQbkSWe5mQfhFFDGzFJvCMQn1y4Rz992RGo=",
            "Token": "3SGtCiyn5Dgyo1oNLp40PMbAKw2G9bLac1eb967f8fef73b570ea3f19bc83f45exJMAgMAA5vutzNHCId6iXbJwRu-DI17Ef0hkHpOPRPaJLojsNddOSlSSNTqT44882gTlAFgSeZVaR2NDCHURBhTsq4YIJoqMj5d22-DFx_yr5tWPVSNF_9KSwvbhO6ANTIuEmCcfTiLyr9mOizm8Npxk_fF_eaFN0grjis9gmoSwgNwfcIWhtlcBci5xsIDYI3rdIdSt-qeuPYrZnm2kZEvSnL3M4kiUIL1IZ0MjrSedMPW4X9g96TLMQvnqPhx7yVZqhT5U_TAoscIgyjXO8kRNfBpRahg5L1hy-vIUKDUqA0BdyFF-4-iKi79XL8S7zA4sl8po9gZHCQsGjxJYSC2CuIlpQjjmnUznsy5rShLT7wFzF-wEJODEp1CzsNzNLta0fcMgOmYAL5VXDuZ7wJQ-BP8rv6S6y5kOs7ZS4HWSdvX3EbqqZ50Xntkz7GQOPWBR8OVaTIH9ryLzDVnPs011ixP-AVSWl9q6rkDWprt_sY3518ZEG4ksqt4ScHy8ioxcsdnI4Wf2mfDtnUV5E6owbGgpkJDbh4GnhRXRNyT2rHQdmjWh7qcTseVhAOpq4Qgs8XZoKL3sN-9VP1G-crRlEZe_dL4CMEoqMDuqmYRxJ1uFzanrn3DNrW5WE0gsmxj6RWFEB68IV9wbeW0NJxiEX47NDrzhEAGptNBX9SJ8P9Xf8OR8CA_qZxIpwn-6vZizN1gOmjeSk96Be1bo0U-z1Vogr9H9oTpXVLQHDrt_Y2IbNw70UZhRgWrU8WJmZunmqvCMqjripSHVLcTHgwXSxemZ7i7RngoRh1GkxYXDngcUFVvVoMVGLDhnJSw_Y5cF-XoMIz-GhFrZrxxFHoLXix5vTp4uenUcX_-R33yFLExfVRexfL5GkiXw94dOUL4K7-NLzRE9uJY6nzng5oR0v1eP_PO-TtfP8FQgiJIp6uGpVWUCAm8tWI-0QnJpVHbwH9IMma8Y65F1EsLBD06XKELijAwsPyFNV2WzijmVvzCtjpNRskG0F2ogmT53RLLvXmJQ2fucSCVb8cqdcNd9tiSwxykqoUfzsfDRphRuAqznWqMK6kbvKkeGE4L_UYju_cgmCjsLi_dzHnn7NA",
            "UpdateTime": null
        }
    }
}
```

