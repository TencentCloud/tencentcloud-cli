**Example 1: 获取合同对比结果web页面**



Input: 

```
tccli ess DescribeContractDiffTaskWebUrl --cli-unfold-argument  \
    --Operator.UserId yDw9iUUgyg36ykr3Ux4GQpt1FPWYQOZC \
    --TaskId yDttgUUckpxxat41UyoAic6CrjE7K0x2
```

Output: 
```
{
    "Response": {
        "RequestId": "s1748918302614730295",
        "WebUrl": "https://embed.test.qian.tencent.cn/contract-compare?embed=1&code=yDt3RUUckpx9s4h8UuFSuGdR9VDNF2lh&channel=TENCENTCLOUD&embedType=CONTRACT_DIFF&businessType=TASK_ID&businessId=yDttgUUckpxxat41UyoAic6CrjE7K0x2"
    }
}
```

